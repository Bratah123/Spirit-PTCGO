import logging
import os
from datetime import datetime
from spirit.network.protocol import WargFlags
from spirit.network.message_names import InboundMsg
from .base import BaseHandler, handle


BENIGN_CLIENT_ERROR_SUBSTRINGS = (
    "Serialized game state can't be loaded while a game is in progress",
    # Stock client bug: AvatarCamRenderTextureController (and Viewport/MirrorReflection)
    # release RenderTextures without unbinding Camera.targetTexture first. Unity
    # self-heals; fires on every match when a real hair item is equipped.
    "Releasing render texture that is set as Camera.targetTexture!",
)


def _is_benign_client_error(reason: str) -> bool:
    return any(sub in reason for sub in BENIGN_CLIENT_ERROR_SUBSTRINGS)


class SystemHandler(BaseHandler):
    @handle(InboundMsg.PING)
    async def handle_ping(self, message, request_id, flags):
        # Respond with Pong using PingPong flag
        response = {"messageName": "Pong"}
        await self.client.send_packet(response, request_id, flags=WargFlags.PING_PONG)

    @handle(InboundMsg.LOG_CLIENT_ERROR)
    async def handle_log_client_error(self, message, request_id, flags):
        error_name = message.get("name", "UnknownError")
        reason = message.get("reason", "No reason provided")
        log_id = message.get("logID", "UnknownLogID")
        debug_info = message.get("debugInfo", {})

        # Known-benign client artifact: down-rank to a single line so it doesn't masquerade
        # as a crash, but still persist it to client_errors.log for the record.
        if _is_benign_client_error(reason):
            first_line = reason.strip().splitlines()[0] if reason.strip() else reason
            logging.info(f"[TCP] [{self.client.addr}] Benign client error (non-fatal): {first_line} (logID={log_id})")
            self._write_client_error_file(error_name, reason, log_id, debug_info)
            return

        # Standard console log
        logging.error(f"\n{'='*50}\n[TCP] [{self.client.addr}] CLIENT CRASH REPORT\n{'='*50}")
        logging.error(f"Error Type : {error_name}")
        logging.error(f"Log ID     : {log_id}")
        logging.error(f"Reason     :\n{reason}\n")
        
        if debug_info:
            logging.error(f"Debug Info :")
            for key, val in debug_info.items():
                logging.error(f"  {key}: {val}")
        logging.error(f"{'='*50}\n")

        self._write_client_error_file(error_name, reason, log_id, debug_info)

        # LogClientError is a fire-and-forget telemetry packet.
        # We do not send a response back.

    def _write_client_error_file(self, error_name, reason, log_id, debug_info):
        """Appends a full client error record to 'client_errors.log' (all severities)."""
        log_file_path = "client_errors.log"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = [
            f"{'='*60}",
            f"[{timestamp}] CLIENT CRASH REPORT from {self.client.addr}",
            f"{'='*60}",
            f"Error Type : {error_name}",
            f"Log ID     : {log_id}",
            f"Reason     :\n{reason}\n"
        ]

        if debug_info:
            log_entry.append("Debug Info :")
            for key, val in debug_info.items():
                log_entry.append(f"  {key}: {val}")
        log_entry.append(f"{'='*60}\n\n")

        log_text = "\n".join(log_entry)

        try:
            with open(log_file_path, "a", encoding="utf-8") as f:
                f.write(log_text)
                f.flush()
        except Exception as e:
            logging.error(f"[System] Failed to write client error to {log_file_path}: {e}")
