import logging

from spirit.network.message_names import InboundMsg, OutboundMsg
from .base import BaseHandler, handle
from spirit.database import economy_data
from spirit.database.async_utils import run_db


class RedemptionHandler(BaseHandler):
    """Handles the client's Shop code redemption flow (ValidateCode / RedeemCodes)."""

    async def _send_invalid(self, code, reason, request_id, message_name=None):
        await self.send({
            "messageName": message_name or OutboundMsg.INVALID_CODE.value,
            "code": code,
            "reason": {"id": reason or "shop.redeemcodes.error.invalidcode"}
        }, request_id)

    async def _sync_player_state(self):
        """Pushes fresh collection + wallet snapshots after a grant."""
        if not self.client.player:
            return
        await self.push_collection()
        await run_db(self.client.player.wallet.refresh_wallet)
        await self.push_wallet()

    @handle(InboundMsg.VALIDATE_CODE)
    async def handle_validate_code(self, message, request_id, flags):
        code = ((message or {}).get("code") or "").strip().upper()
        logging.info(f"[TCP] [{self.client.addr}] Client validating redemption code: {code}")

        if not self.client.player:
            return await self._send_invalid(code, None, request_id)

        ok, reward, reason = await run_db(economy_data.check_code, code, self.client.player.account_id)
        if not ok:
            return await self._send_invalid(code, reason, request_id)

        await self.send({
            "messageName": OutboundMsg.CODE_IS_VALID.value,
            "code": code,
            "products": list((reward or {}).get("products", {}).keys()),
            "couponGroup": code,
            "maxRedemptionsForGroup": None
        }, request_id)

    @handle(InboundMsg.REDEEM_CODES)
    async def handle_redeem_codes(self, message, request_id, flags):
        codes = (message or {}).get("codes") or []
        logging.info(f"[TCP] [{self.client.addr}] Client redeeming codes: {codes}")

        if not self.client.player:
            for code in codes:
                await self._send_invalid(code, None, request_id,
                                         message_name=OutboundMsg.CODE_REDEMPTION_FAILURE.value)
            return

        account_id = self.client.player.account_id
        any_success = False
        for code in codes:
            code = (code or "").strip().upper()
            ok, reward, reason = await run_db(economy_data.redeem_code, code, account_id)
            if ok:
                any_success = True
                await self.send({
                    "messageName": OutboundMsg.CODE_SUCCESSFULLY_REDEEMED.value,
                    "code": code
                }, request_id)
                logging.info(f"[TCP] Code {code} redeemed by {account_id}: {reward}")
            else:
                await self._send_invalid(code, reason, request_id,
                                         message_name=OutboundMsg.CODE_REDEMPTION_FAILURE.value)

        if any_success:
            await self._sync_player_state()
