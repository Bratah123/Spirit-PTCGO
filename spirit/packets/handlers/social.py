import logging
import uuid
import json

from spirit.network.message_names import InboundMsg, OutboundMsg
from spirit.database.accounts import get_account_by_username, get_account_by_id
from spirit.database.async_utils import run_db
from spirit.database.social import add_friend_relationship, remove_friend_relationship, get_friends_by_account_id
from spirit.game.models.social import Friend, FriendListStatus
from .base import BaseHandler, handle

# RoomType.Lobby == 0; the client's AvailableRooms handler (s.w) auto-joins a
# random Lobby-typed room, which keeps JoinedRooms[0] a safe switch-back target
# when the game chat room is removed at end of game (T.W).
LOBBY_ROOMS = [
    {"roomID": "Lobby_Spirit_1", "displayName": "Spirit Lobby", "roomType": 0},
]


class SocialHandler(BaseHandler):
    def _chat_rooms(self, client=None):
        """Set of room IDs the client handler has joined."""
        client = client or self.client
        if not hasattr(client, "chat_rooms"):
            client.chat_rooms = set()
        return client.chat_rooms

    def _room_member_clients(self, room_id):
        return [
            c for c in self.client.server.clients
            if getattr(c, "player", None) and room_id in getattr(c, "chat_rooms", ())
        ]

    def _chat_user_info(self, client=None):
        player = (client or self.client).player
        return {"accountID": player.account_id, "displayName": player.screen_name}

    @handle(InboundMsg.PRIVATE_CHAT)
    async def handle_private_chat(self, message, request_id, flags):
        target_id = message.get("accountID")
        chat_msg = message.get("message")
        purpose = message.get("purpose", "")

        logging.info(f"[TCP] [{self.client.addr}] Chat from '{self.client.player.screen_name}' to '{target_id}': {chat_msg}")

        target_client = self.online_client(target_id)

        # Build notification packet
        notify_packet = {
            "messageName": OutboundMsg.NOTIFY_PRIVATE_CHAT.value,
            "userInfo": {
                "accountID": self.client.player.account_id,
                "displayName": self.client.player.screen_name
            },
            "toUserInfo": {
                "accountID": target_id,
                "displayName": target_client.player.screen_name if target_client else "Offline Player"
            },
            "message": chat_msg,
            "purpose": purpose,
            "targetWasOnline": target_client is not None
        }

        # 1. Echo back to sender so they see their own message in the UI
        await self.client.send_packet(notify_packet, 0)

        # 2. Route to target if online
        if target_client:
            await target_client.send_packet(notify_packet, 0)

    @handle(InboundMsg.PUBLIC_ROOMS)
    async def handle_public_rooms(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Public Rooms.")
        await self.send({
            "messageName": OutboundMsg.AVAILABLE_ROOMS.value,
            "rooms": list(LOBBY_ROOMS),
        }, request_id)

    @handle(InboundMsg.JOIN_ROOM)
    async def handle_join_room(self, message, request_id, flags):
        room_id = message.get("roomID")
        room = next((r for r in LOBBY_ROOMS if r["roomID"] == room_id), None)
        if room is None or not self.client.player:
            return
        logging.info(f"[TCP] [{self.client.addr}] Joining chat room '{room_id}'.")
        notify = {
            "messageName": OutboundMsg.NOTIFY_JOIN.value,
            "roomID": room_id,
            "userInfo": self._chat_user_info(),
        }
        for member in self._room_member_clients(room_id):
            await member.send_packet(notify, 0)
        self._chat_rooms().add(room_id)
        # T.B registers the room + selects it; it drops the joiner from members.
        await self.send({
            "messageName": OutboundMsg.CHAT_CONNECTED.value,
            "room": dict(room),
            "members": [
                self._chat_user_info(c) for c in self._room_member_clients(room_id)
            ],
            "messageHistory": [],
        }, request_id)

    @handle(InboundMsg.LEAVE_ROOM)
    async def handle_leave_room(self, message, request_id, flags):
        room_id = message.get("roomID")
        self._chat_rooms().discard(room_id)
        await self.send({
            "messageName": OutboundMsg.CHAT_DISCONNECTED.value,
            "roomID": room_id,
        }, request_id)
        if not self.client.player:
            return
        notify = {
            "messageName": OutboundMsg.NOTIFY_LEAVE.value,
            "roomID": room_id,
            "accountID": self.client.player.account_id,
        }
        for member in self._room_member_clients(room_id):
            await member.send_packet(notify, 0)

    @handle(InboundMsg.CHAT)
    async def handle_room_chat(self, message, request_id, flags):
        room_id = message.get("roomID")
        chat_msg = message.get("message", "")
        if not self.client.player or room_id not in self._chat_rooms():
            return
        # The sender renders their own message from this notify too — no echo path.
        notify = {
            "messageName": OutboundMsg.NOTIFY_CHAT.value,
            "roomID": room_id,
            "userInfo": self._chat_user_info(),
            "message": chat_msg,
        }
        for member in self._room_member_clients(room_id):
            await member.send_packet(notify, 0)

    @handle(InboundMsg.QUESTS_ENABLED)
    async def handle_quests_enabled(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client checking if Quests are enabled.")
        pass

    @handle(InboundMsg.GET_FRIEND_ROSTER)
    async def handle_get_friend_roster(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Friend Roster.")

        if not self.client.player:
            return

        # Dynamically check online status for the roster
        for friend_id, friend_obj in self.client.player.friends_list.friends.items():
            friend_obj.presence = "Online" if self.online_client(friend_id) else "Offline"

        response = self.client.player.get_friends_roster_data()
        response["messageName"] = OutboundMsg.FRIEND_ROSTER.value

        await self.send(response, request_id)

    async def _send_friend_added(self, client, friend: Friend, request_id=0):
        """Adds the friend to the client's model and pushes FRIEND_ADDED."""
        client.player.friends_list.add_friend(friend)
        await client.send_packet({
            "messageName": OutboundMsg.FRIEND_ADDED.value,
            "friend": friend.serialize()
        }, request_id)

    async def _notify_target_friend_added(self, target_id):
        """If the target is online, registers the sender in their model and notifies them."""
        target_client = self.online_client(target_id)
        if target_client:
            entry = Friend(self.client.player.account_id, self.client.player.screen_name,
                           FriendListStatus.Friends, presence="Online")
            await self._send_friend_added(target_client, entry, 0)

    @handle(InboundMsg.CREATE_FRIEND_INVITATION)
    async def handle_create_friend_invitation(self, message, request_id, flags):
        target_name = message.get("displayName")
        logging.info(f"[TCP] [{self.client.addr}] Player '{self.client.player.screen_name}' inviting '{target_name}'.")

        target_account = await run_db(get_account_by_username, target_name)
        if not target_account:
            return await self._send_social_error(request_id, f"User '{target_name}' not found.")

        target_id = target_account['account_id']
        sender_id = self.client.player.account_id

        if target_id == sender_id:
            return await self._send_social_error(request_id, "You cannot invite yourself.")

        # 1. Check if the target has already invited the sender (Mutual Invite)
        existing_friends = await run_db(get_friends_by_account_id, target_id)
        is_mutual = any(f['friend_id'] == sender_id and f['status'] == FriendListStatus.Invited for f in existing_friends)

        if is_mutual:
            logging.info(f"[TCP] Mutual invitation detected between '{self.client.player.screen_name}' and '{target_name}'. Promoting to Friends.")

            def _befriend_both():
                add_friend_relationship(sender_id, target_id, FriendListStatus.Friends)
                add_friend_relationship(target_id, sender_id, FriendListStatus.Friends)
            await run_db(_befriend_both)

            new_friend = Friend(target_id, target_name, FriendListStatus.Friends, presence="Online")
            await self._send_friend_added(self.client, new_friend, request_id)
            await self._notify_target_friend_added(target_id)
            return

        # 2. Standard Invitation Logic
        await run_db(add_friend_relationship, sender_id, target_id, FriendListStatus.Invited)

        # Notify Target if online (triggers badge "1" and popup)
        target_client = self.online_client(target_id)
        if target_client:
            invite_payload = {
                "name": OutboundMsg.FRIEND_INVITATION.value,
                "value": {
                    "friend": {
                        "accountID": sender_id,
                        "displayName": self.client.player.screen_name
                    }
                }
            }

            notification_packet = {
                "messageName": OutboundMsg.NOTIFICATION.value,
                "notificationID": str(uuid.uuid4()),
                "payload": json.dumps(invite_payload),
                "notificationType": 0 # Normal
            }
            await target_client.send_packet(notification_packet, 0)

        # Sender sees them as Invited
        new_friend = Friend(target_id, target_name, FriendListStatus.Invited, presence="Offline")
        await self._send_friend_added(self.client, new_friend, request_id)

    @handle(InboundMsg.ACCEPT_FRIEND_INVITATION)
    async def handle_accept_friend_invitation(self, message, request_id, flags):
        target_id = message.get("accountID")
        logging.info(f"[TCP] [{self.client.addr}] Player '{self.client.player.screen_name}' accepting invitation from '{target_id}'.")

        my_id = self.client.player.account_id

        def _accept_sync():
            add_friend_relationship(my_id, target_id, FriendListStatus.Friends)
            add_friend_relationship(target_id, my_id, FriendListStatus.Friends)
            return get_account_by_id(target_id)
        friend_data = await run_db(_accept_sync)
        friend_name = friend_data['screen_name'] if friend_data else "Unknown"

        await self._notify_target_friend_added(target_id)

        new_friend = Friend(target_id, friend_name, FriendListStatus.Friends, presence="Online")
        await self._send_friend_added(self.client, new_friend, request_id)

    async def _remove_mutual_friendship(self, target_id):
        """Removes both DB rows and model entries; notifies the target if online."""
        my_id = self.client.player.account_id

        def _remove_both():
            remove_friend_relationship(my_id, target_id)
            remove_friend_relationship(target_id, my_id)
        await run_db(_remove_both)

        self.client.player.friends_list.remove_friend(target_id)

        target_client = self.online_client(target_id)
        if target_client:
            target_client.player.friends_list.remove_friend(my_id)
            await target_client.send_packet({
                "messageName": OutboundMsg.FRIEND_REMOVED.value,
                "accountID": my_id
            }, 0)

    @handle(InboundMsg.DECLINE_FRIEND_INVITATION)
    async def handle_decline_friend_invitation(self, message, request_id, flags):
        await self._remove_mutual_friendship(message.get("accountID"))

    @handle(InboundMsg.REMOVE_FRIEND)
    async def handle_remove_friend(self, message, request_id, flags):
        target_id = message.get("accountID")
        await self._remove_mutual_friendship(target_id)

        await self.client.send_packet({
            "messageName": OutboundMsg.FRIEND_REMOVED.value,
            "accountID": target_id
        }, request_id)

    @handle(InboundMsg.SET_CURRENT_PRESENCE)
    async def handle_set_current_presence(self, message, request_id, flags):
        presence = message.get("status", "Online")
        await self.broadcast_presence(presence)

    async def broadcast_presence(self, presence):
        if not self.client.player:
            return

        presence_packet = {
            "messageName": OutboundMsg.FRIEND_PRESENCE.value,
            "accountID": self.client.player.account_id,
            "presence": presence
        }

        for friend_id in self.client.player.friends_list.friends:
            target_client = self.online_client(friend_id)
            if target_client:
                await target_client.send_packet(presence_packet, 0)

    async def _send_social_error(self, request_id, message):
        await self.client.send_packet({
            "messageName": OutboundMsg.FRIEND_ERROR.value,
            "error": message
        }, request_id)

    @handle(InboundMsg.GET_QUESTS)
    async def handle_get_quests(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] Client requested Quests.")
        await self.send({
            "messageName": OutboundMsg.QUESTS.value,
            "quests": []
        }, request_id)
