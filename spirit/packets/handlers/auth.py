import logging

from spirit.network.protocol import WargFlags
from spirit.network.message_names import InboundMsg, OutboundMsg
from spirit.database.accounts import get_account_by_username, create_account, verify_password
from spirit.game.attributes import AttrID
from spirit.game.season_manager import VersusSeasonManager
from spirit.game.account_attributes import build_account_attributes, anchor_versus_animation
from .base import BaseHandler, handle
from spirit.server.state import PENDING_TICKETS, sweep_expired_tickets
from .social import SocialHandler
from spirit.game.models.player import Player
from spirit.database.async_utils import run_db
from spirit.database.daily_rewards import process_daily_login
from spirit.game.daily_rewards import DailyRewardManager


def _get_or_create_account(username, password):
    account = get_account_by_username(username)
    if not account:
        account = create_account(username, password)
    return account


class AuthHandler(BaseHandler):
    @handle(InboundMsg.AUTHENTICATE_CAS_TICKET)
    async def handle_authenticate_cas_ticket(self, message, request_id, flags):
        # CAS Authentication (Modern PC Login)

        username = str(message.get("accountName", ""))
        ticket = str(message.get("serviceTicket", ""))
        service = str(message.get("serviceName", ""))

        logging.info(f"[TCP] User {username} is attempting CAS login with ticket {ticket} for service {service}")
        
        # 1. Verify Ticket
        sweep_expired_tickets()
        entry = PENDING_TICKETS.get(ticket)
        if entry is None or entry[0] != username:
            logging.warning(f"[TCP] [{self.client.addr}] Invalid CAS ticket: {ticket} for user: {username}")
            return await self._send_auth_failed(request_id, "Invalid CAS Ticket.")

        # Consume the ticket
        del PENDING_TICKETS[ticket]

        # 2. Look up the account
        account = await run_db(get_account_by_username, username)
        if not account:
            # This shouldn't happen if the ticket was issued, but safety first
            return await self._send_auth_failed(request_id, "Account sync error.")

        # 3. Success!
        logging.info(f"[TCP] [{self.client.addr}] User '{username}' successfully authenticated via CAS.")
        await self._send_auth_success(request_id, account)

    @handle(InboundMsg.START_AUTH)
    async def handle_start_authentication(self, message, request_id, flags):
        auth_type = message.get("authType", "Unknown")
        logging.info(f"[TCP] [{self.client.addr}] Client started authentication sequence. Type: {auth_type}")
        
        if auth_type == "DeviceID":
            logging.info(f"[TCP] [{self.client.addr}] Bypassing DeviceID token exchange. Forcing Auth Success.")
            
            # Auto-register a guest account based on their IP or a dummy ID for now
            device_id = f"guest_{self.client.addr[0]}"
            account = await run_db(_get_or_create_account, device_id, "guest_password")

            return await self._send_auth_success(request_id, account)

        response = {
            "messageName": OutboundMsg.REQ_AUTH_TOKEN.value
        }
        await self.client.send_packet(response, request_id, flags=WargFlags.CLEAR)

    @handle(InboundMsg.AUTH_GAS_TOKEN)
    async def handle_gas_auth_token(self, message, request_id, flags):
        # PC Login
        # Currently treating userID as the username field because the client's packet format is ambiguous
        username = str(message.get("userID", ""))
        password = str(message.get("token", ""))

        logging.info(f"[TCP] User {username} is attempting to login...")
        
        account = await run_db(get_account_by_username, username)

        # Auto-Register if it doesn't exist
        if not account:
            logging.info(f"[TCP] [{self.client.addr}] Auto-registering new user: {username}")
            account = await run_db(create_account, username, password)
            if not account:
                return await self._send_auth_failed(request_id, "Could not create account. Please try again.")

        # if account existed or was just created
        if not await run_db(verify_password, account['password_hash'], password):
            logging.warning(f"[TCP] [{self.client.addr}] Failed login attempt for user: {username}")
            return await self._send_auth_failed(request_id, "Incorrect password. Please try again.")

        logging.info(f"[TCP] [{self.client.addr}] User '{username}' successfully authenticated.")
        await self._send_auth_success(request_id, account)

    @handle(InboundMsg.AUTH_GAS_GUEST)
    async def handle_gas_guest(self, message, request_id, flags):
        # Guest Login (Usually auto-creates a temporary account based on device ID)
        device_id = message.get("uniqueID", "guest_unknown")
        account = await run_db(_get_or_create_account, device_id, "guest_password")
        await self._send_auth_success(request_id, account)

    @handle(InboundMsg.AUTH_GAS_MOBILE)
    async def handle_gas_mobile(self, message, request_id, flags):
        # Mobile Login
        mobile_id = message.get("mobileID", "mobile_unknown")
        account = await run_db(_get_or_create_account, mobile_id, "mobile_password")
        await self._send_auth_success(request_id, account)

    async def _send_auth_success(self, request_id, account_data):
        # Concurrent Login Prevention
        account_id = account_data['account_id']
        username = account_data['username']

        other_client = self.online_client(account_id, exclude_self=True)
        if other_client:
            logging.warning(f"[TCP] [{self.client.addr}] Prevented concurrent login: User '{username}' is already logged in on client {other_client.addr}")
            await self._send_auth_failed(request_id, "The account you are trying to login is already online.")
            return

        # One thread hop for the whole DB-heavy login load (player profile,
        # account attributes, daily login progress).
        def _load_login_state():
            player = Player(account_data)
            # Anchor the versus-ladder animation to current points BEFORE building
            # attributes, so a relog never replays the points/reward animation.
            anchor_versus_animation(account_id)
            attributes = build_account_attributes(account_id)
            daily_info = process_daily_login(account_id)
            return player, attributes, daily_info

        player, account_attributes, daily_info = await run_db(_load_login_state)
        self.client.player = player

        # Notify friends that we are online
        social_handler = SocialHandler(self.client)
        await social_handler.broadcast_presence("Online")

        # AuthenticationSuccessful
        response = {
            "messageName": OutboundMsg.AUTH_SUCCESS.value,
            "account": {
                "username": account_data['username'],
                "accountID": account_data['account_id'],
                "attributes": account_attributes
            },
            "sessionID": self.client.session_id,
            "supplementaryInfo": None
        }
        await self.client.send_packet(response, request_id, flags=WargFlags.CLEAR)

        # EulaSuccessful
        await self.client.send_packet({
            "messageName": OutboundMsg.EULA_SUCCESSFUL.value,
            "version": 1
        }, 0)

        # CohortsForAccount
        await self.client.send_packet({
            "messageName": OutboundMsg.COHORTS_FOR_ACCOUNT.value,
            "cohorts": {},
            "redirectScenes": {},
            "cohortFeatures": []
        }, 0)

        # PlayerNotInGame
        await self.client.send_packet({
            "messageName": OutboundMsg.PLAYER_NOT_IN_GAME.value
        }, 0)

        # NetworkStatusIndicatorConfiguration
        await self.client.send_packet({
            "messageName": OutboundMsg.NETWORK_STATUS_INDICATOR_CONFIGURATION.value,
            "pingWarningThreshold": 500,
            "pingErrorThreshold": 1000
        }, 0)

        # DefaultTrainerChallengeDeckMessage
        await self.client.send_packet({
            "messageName": OutboundMsg.DEFAULT_TRAINER_CHALLENGE_DECK_MESSAGE.value,
            "defaultDeckName": "Mental Might"
        }, 0)

        # CurrentVersusSeason
        active_season = VersusSeasonManager().get_active_season()
        season_payload = active_season.to_dict() if active_season else {
            "seasonID": "Season1",
            "startTime": 0,
            "endTime": 4102444800000, # Year 2100
            "description": {"id": "SpiritPTCGO Season"},
            "tiers": [],
            "resetRewardID": ""
        }
        await self.client.send_packet({
            "messageName": OutboundMsg.CURRENT_VERSUS_SEASON.value,
            "versusSeason": season_payload
        }, 0)

        # CurrentDailyRewardTrack
        await self.client.send_packet({
            "messageName": OutboundMsg.CURRENT_DAILY_REWARD_TRACK.value,
            "dailyRewardTrack": {
                "name": "Standard Track",
                "rewardTiers": [
                    {
                        "wins": 1,
                        "rewards": [
                            {
                                "name": "5 Tokens",
                                "rewardType": "Currency",
                                "rewardAmount": 5
                            }
                        ],
                        "isDefault": True,
                        "isSpecial": False
                    }
                ],
                "isDefault": True
            },
            "nextExpiry": 4102444800000
        }, 0)

        # QuestConfigurationUpdated
        await self.client.send_packet({
            "messageName": OutboundMsg.QUEST_CONFIGURATION_UPDATED.value,
            "questConfiguration": {
                "xpLevelMap": {"1": 100, "2": 200},
                "levelTierMap": {"1": 1},
                "affinityToAffinityLevelRewardsMap": {},
                "nextQuestAvailableTime": 4102444800000,
                "levelActiveQuestsMap": {"1": 1}
            }
        }, 0)

        # DailyLogin — weeksRewards outer array = days; timestamp = next reward time in ms
        await self.client.send_packet({
            "messageName": OutboundMsg.DAILY_LOGIN.value,
            "activations": daily_info["activations"],
            "timestamp": daily_info["nextRewardTimestampMs"],
            "lastLoginTimestamp": daily_info["nextRewardTimestampMs"],
            "rewardDay": daily_info["rewardDay"],
            "weeksRewards": DailyRewardManager().weeks_rewards(daily_info["activations"]),
            "firstDailyLogin": daily_info["firstDailyLogin"]
        }, 0)

        # AccountPropertiesUpdated
        await self.client.send_packet({
            "messageName": OutboundMsg.ACCOUNT_PROPERTIES_UPDATED.value,
            "accountID": account_data['account_id'],
            "attributes": [
                {"name": AttrID.FRIEND_CHAT_MODE.value, "value": "OpenChat"},
                {"name": AttrID.FRIEND_MODE.value, "value": "Open"},
                {"name": AttrID.FRIEND_TRADE_MODE.value, "value": "Free"},
                {"name": AttrID.GAME_CHAT_MODE.value, "value": "OpenChat"},
                {"name": AttrID.PUBLIC_CHAT_MODE.value, "value": "OpenChat"},
                {"name": AttrID.SHOPPING_MODE.value, "value": "Open"},
                {"name": AttrID.TRADE_MODE.value, "value": "Free"},
                {"name": AttrID.PRIVATE_MESSAGING_MODE.value, "value": "OpenChat"},
                {"name": AttrID.DECK_SHARE_MODE.value, "value": "Everybody"},
            ]
        }, 0)

        # DynamicVersions (Push initial versions)
        await self.client.send_packet({
            "messageName": OutboundMsg.DYNAMIC_VERSIONS.value,
            "versionData": {
                "major_version_number": "1",
                "minor_version_number": "0",
                "content_data_version": "1",
                "content_data_version_id": "0",
                "cachedDisplayVersion": "1",
                "cachedCollectionVersion": "1",
                "androidpatchversion": "1",
                "iospatchversion": "1",
                "lastUpdatedAtVersion": "1",
                "opponentsDataVersion": "1",
                "progressionDataVersion": "1",
                "cachedDarkenDataVersion": "1",
                "LatestMacPatcherVersion": "1",
                "LatestWindowsPatcherVersion": "1",
                "LatestMacClientVersion": "1",
                "LatestWindowsClientVersion": "1"
            }
        }, 0)

    async def _send_auth_failed(self, request_id, reason_text):
        """Sends an AuthenticationFailed message back to the client."""
        response = {
            "messageName": OutboundMsg.AUTH_FAILED.value,
            "reason": {
                "token": reason_text,
                "bundle": {"en": reason_text}
            }
        }
        await self.client.send_packet(response, request_id, flags=WargFlags.CLEAR)
