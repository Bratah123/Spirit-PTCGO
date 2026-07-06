import logging
import time

from spirit.network.protocol import WargFlags
from spirit.network.message_names import InboundMsg, OutboundMsg
from .base import BaseHandler, handle
from .shop import build_item
from spirit.database import economy_data
from spirit.database.async_utils import run_db
from spirit.database.player_data import get_merged_collection_payload, set_archetype_flag
from spirit.game.attributes import AttrID

EMPTY_GUID = "00000000-0000-0000-0000-000000000000"
# Lot lifetime shown to the client; offers never expire server-side for now
LOT_LIFETIME_MS = 30 * 24 * 3600 * 1000


class TradeHandler(BaseHandler):
    """Implements the Trade Room 'lots' protocol (B.M command factory)."""

    def _account_id(self):
        return self.client.player.account_id if self.client.player else None

    def _offer_to_lot(self, offer):
        """Serializes a TradeOffer row to the client's Lot (B.m) JSON shape."""
        items = []
        for guid, count in offer["offering"].items():
            for _ in range(int(count)):
                items.append(build_item(offer["sender_id"], guid, is_tradable=True))
        return {
            "id": offer["offer_id"],
            "items": items,
            "price": 0.0,
            "owner": offer["sender_id"],
            "ownerName": offer.get("sender_name") or "",
            "lockID": EMPTY_GUID,
            "lockedBy": EMPTY_GUID,
            "lockedByName": "",
            "expirationDate": int(time.time() * 1000) + LOT_LIFETIME_MS,
            "expirationHR": "30 days",
            "expirationType": 0,
            "isDeck": False,
            "cardPrice": offer["requesting"],
            "message": ""
        }

    async def _send_error(self, message_name, reason, request_id):
        await self.send({
            "messageName": message_name,
            "error": {"id": reason}
        }, request_id)

    async def _sync_collection(self, client):
        """Pushes a collection refresh to any online client (self or trade partner)."""
        if not client.player:
            return
        payload = await run_db(get_merged_collection_payload, client.player.account_id)
        await client.send_packet({
            "messageName": OutboundMsg.COLLECTION_COUNT_FOUND.value,
            "collectionCountList": payload
        }, 0, flags=WargFlags.CLEAR)

    # ------------------------------------------------------------- Count handshake
    # Each trade tab first asks for a count, then requests the page using it as
    # the limit. Reply MUST carry the true total tied to the request_id — the
    # client renders empty on count 0 and never sends the pagination request.

    @handle(InboundMsg.VIEW_MY_LOTS_COUNT)
    async def handle_view_my_lots_count(self, message, request_id, flags):
        account_id = self._account_id()
        count = await run_db(economy_data.count_trade_offers, sender_id=account_id) if account_id else 0
        await self.send({
            "messageName": OutboundMsg.MY_LOTS_RETRIEVED_COUNT.value,
            "count": count
        }, request_id)

    @handle(InboundMsg.VIEW_ALL_PRIVATE_TRADES_COUNT)
    async def handle_view_private_trades_count(self, message, request_id, flags):
        account_id = self._account_id()
        count = await run_db(economy_data.count_trade_offers, recipient_id=account_id) if account_id else 0
        await self.send({
            "messageName": OutboundMsg.PRIVATE_LOTS_RETRIEVED_COUNT.value,
            "count": count
        }, request_id)

    @handle(InboundMsg.VIEW_ALL_PUBLIC_TRADES_COUNT)
    async def handle_view_public_trades_count(self, message, request_id, flags):
        account_id = self._account_id()
        count = await run_db(economy_data.count_trade_offers, public=True, exclude_sender_id=account_id)
        await self.send({
            "messageName": OutboundMsg.LOTS_RETRIEVED_COUNT.value,
            "count": count
        }, request_id)

    @handle(InboundMsg.VIEW_TRADE_HISTORY_2_COUNT)
    async def handle_view_trade_history_count(self, message, request_id, flags):
        account_id = self._account_id()
        count = len(await run_db(self._trade_history, account_id)) if account_id else 0
        await self.send({
            "messageName": OutboundMsg.TRADE_HISTORY_RETRIEVED_COUNT.value,
            "count": count
        }, request_id)

    # ------------------------------------------------------------- Views

    @handle(InboundMsg.VIEW_ALL_PUBLIC_TRADES_WITH_PAGINATION)
    async def handle_view_public_trades(self, message, request_id, flags):
        account_id = self._account_id()
        offset = (message or {}).get("offset", 0)
        limit = (message or {}).get("limit", 50)

        offers, _total = await run_db(
            economy_data.list_trade_offers,
            public=True, exclude_sender_id=account_id, offset=offset, limit=limit)

        await self.send({
            "messageName": OutboundMsg.LOTS_RETRIEVED.value,
            "lots": [self._offer_to_lot(o) for o in offers]
        }, request_id)

    @handle(InboundMsg.VIEW_ALL_PRIVATE_TRADES_WITH_PAGINATION)
    async def handle_view_private_trades(self, message, request_id, flags):
        account_id = self._account_id()
        if not account_id:
            return
        offset = (message or {}).get("offset", 0)
        limit = (message or {}).get("limit", 50)

        offers, _total = await run_db(
            economy_data.list_trade_offers,
            recipient_id=account_id, offset=offset, limit=limit)

        await self.send({
            "messageName": OutboundMsg.PRIVATE_LOTS_RETRIEVED.value,
            "lots": [self._offer_to_lot(o) for o in offers],
            "counterOffers": []
        }, request_id)

    @handle(InboundMsg.VIEW_MY_LOTS_WITH_PAGINATION)
    async def handle_view_my_lots(self, message, request_id, flags):
        account_id = self._account_id()
        if not account_id:
            return
        offset = (message or {}).get("offset", 0)
        limit = (message or {}).get("limit", 50)

        offers, _total = await run_db(
            economy_data.list_trade_offers,
            sender_id=account_id, offset=offset, limit=limit)

        await self.send({
            "messageName": OutboundMsg.MY_LOTS_RETRIEVED.value,
            "lots": [self._offer_to_lot(o) for o in offers],
            "offers": []
        }, request_id)

    @handle(InboundMsg.SEARCH_FOR_LOTS)
    async def handle_search_for_lots(self, message, request_id, flags):
        account_id = self._account_id()
        wanted = {str(g).lower() for g in (message or {}).get("archetypes", [])}

        offers, _total = await run_db(economy_data.list_trade_offers, public=True, limit=500)
        matches = []
        for o in offers:
            if o["sender_id"] == account_id:
                continue
            offered_guids = {g.lower() for g in o["offering"].keys()}
            if not wanted or wanted & offered_guids:
                matches.append(o)

        await self.send({
            "messageName": OutboundMsg.LOTS_RETRIEVED.value,
            "lots": [self._offer_to_lot(o) for o in matches]
        }, request_id)

    # ------------------------------------------------------------- Mutations

    @handle(InboundMsg.CREATE_LOT_WITH_ARCHETYPES)
    async def handle_create_lot(self, message, request_id, flags):
        account_id = self._account_id()
        if not account_id:
            return
        message = message or {}

        offering = self._normalize_counts(message.get("forTrade"))
        requesting = self._normalize_counts(message.get("toReceive"))
        private_to = message.get("privateTo")
        if private_to in (None, "", EMPTY_GUID):
            private_to = None

        logging.info(f"[TCP] [{self.client.addr}] CreateLot: offering={offering} "
                     f"requesting={requesting} privateTo={private_to}")

        offer, error = await run_db(
            economy_data.create_trade_offer,
            sender_id=account_id,
            offering=offering,
            requesting=requesting,
            recipient_id=private_to
        )
        if error:
            return await self._send_error(OutboundMsg.ERROR_CREATING_LOT.value, error, request_id)

        await self.send({
            "messageName": OutboundMsg.LOT_CREATED.value,
            "lotID": offer["offer_id"]
        }, request_id)

        # Nudge a private recipient who is online
        if private_to:
            recipient = self.online_client(private_to)
            if recipient and self.client.player:
                await recipient.send_packet({
                    "messageName": "LotCreatedForYou",
                    "byUserName": self.client.player.screen_name or self.client.player.username
                }, 0, flags=WargFlags.CLEAR)

    @handle(InboundMsg.REMOVE_LOT)
    async def handle_remove_lot(self, message, request_id, flags):
        account_id = self._account_id()
        lot_id = (message or {}).get("lotID", "")

        if not account_id or not await run_db(economy_data.cancel_trade_offer, lot_id, account_id):
            return await self._send_error(
                OutboundMsg.ERROR_REMOVING_LOT.value,
                "trade.errorCreatingLotDialog.body", request_id)

        await self.send({
            "messageName": OutboundMsg.LOT_REMOVED.value,
            "lotID": lot_id,
            "reason": "Removed"
        }, request_id)

    @handle(InboundMsg.ACCEPT_TRADE)
    async def handle_accept_trade(self, message, request_id, flags):
        account_id = self._account_id()
        lot_id = (message or {}).get("lotID", "")
        if not account_id:
            return

        offer, error = await run_db(economy_data.accept_trade_offer, lot_id, account_id)
        if error:
            return await self._send_error(OutboundMsg.ERROR_PURCHASING_LOT.value, error, request_id)

        logging.info(f"[TCP] Trade {lot_id} accepted by {account_id} "
                     f"(from {offer['sender_id']}).")

        await self.send({
            "messageName": OutboundMsg.LOT_SOLD.value,
            "lotID": lot_id
        }, request_id)
        await self._sync_collection(self.client)

        # Notify the lot owner if they are online
        owner_client = self.online_client(offer["sender_id"])
        if owner_client:
            await owner_client.send_packet({
                "messageName": OutboundMsg.LOT_SOLD.value,
                "lotID": lot_id
            }, 0, flags=WargFlags.CLEAR)
            await self._sync_collection(owner_client)

    def _trade_history(self, account_id):
        """Completed trades this account was party to (sender or accepter)."""
        offers, _ = economy_data.list_trade_offers(status="accepted", limit=500)
        return [o for o in offers if account_id in (o["sender_id"], o["accepted_by"])]

    @handle(InboundMsg.VIEW_TRADE_HISTORY_2)
    async def handle_view_trade_history(self, message, request_id, flags):
        account_id = self._account_id()
        if not account_id:
            return
        offset = int((message or {}).get("offset", 0))
        limit = int((message or {}).get("limit", 50))
        history = (await run_db(self._trade_history, account_id))[offset:offset + limit]
        await self.send({
            "messageName": OutboundMsg.TRADE_HISTORY_RETRIEVED.value,
            "offset": offset,
            "history": [self._offer_to_lot(o) for o in history]
        }, request_id)

    @staticmethod
    def _normalize_counts(value):
        """Accepts {guid: count} or [guid, ...] and returns {guid: count}."""
        if isinstance(value, dict):
            return {str(k): int(v) for k, v in value.items()}
        counts = {}
        for guid in value or []:
            guid = str(guid)
            counts[guid] = counts.get(guid, 0) + 1
        return counts

    @handle(InboundMsg.SET_ARCHETYPE_FOR_TRADE_COUNT)
    async def handle_set_archetype_for_trade_count(self, message, request_id, flags):
        account_id = self._account_id()
        if not account_id:
            return
        message = message or {}
        archetype_id = message.get("archetypeID")
        for_trade = message.get("forTrade", 0)

        if archetype_id:
            await run_db(set_archetype_flag, account_id, archetype_id, for_trade=for_trade)
            await self.send({
                "messageName": OutboundMsg.ARCHETYPE_FOR_TRADE_SET.value,
                "archetypeID": archetype_id,
                "forTrade": for_trade
            }, request_id)

    @handle(InboundMsg.SET_ARCHETYPE_REVIEW)
    async def handle_set_archetype_review(self, message, request_id, flags):
        account_id = self._account_id()
        if not account_id:
            return
        message = message or {}
        archetype_id = message.get("archetypeID")
        review = message.get("review")
        if review is None:
            review = message.get("forTrade", 0)

        if archetype_id:
            await run_db(set_archetype_flag, account_id, archetype_id, review=review)
            await self.send({
                "messageName": OutboundMsg.ARCHETYPE_REVIEW_SET.value,
                "archetypeID": archetype_id,
                "review": review
            }, request_id)

    @handle(InboundMsg.GET_CREATE_LOT_PRICES)
    async def handle_get_create_lot_prices(self, message, request_id, flags):
        prices = {
            0: {"name": AttrID.TRAINER_TOKENS.value, "value": 8}, # 8 hours
            1: {"name": AttrID.TRAINER_TOKENS.value, "value": 24}, # 24 hours
            2: {"name": AttrID.TRAINER_TOKENS.value, "value": 48} # 48 hours
        }
        await self.send({
            "messageName": OutboundMsg.CREATE_LOT_PRICES.value,
            "prices": prices
        }, request_id)
