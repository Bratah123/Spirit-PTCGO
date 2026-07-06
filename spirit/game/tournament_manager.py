import logging
import time
import uuid

from typing import List, Optional

FAR_FUTURE_MS = 4102444800000  # 2100-01-01

# Tournament lifecycle states (mirrors the client's States enum, computed from times)
STATE_BEFORE_PREVIEW = "BeforePreview"
STATE_PREVIEW = "Preview"
STATE_OPEN = "Open"
STATE_ENTRY_CLOSED = "EntryClosed"
STATE_RESOLVED = "Resolved"
STATE_HIDDEN = "Hidden"


def now_ms() -> int:
    return int(time.time() * 1000)


def _loc(text) -> dict:
    """LocalizableText: the client localizer renders unknown IDs verbatim."""
    if isinstance(text, dict):
        return text
    return {"id": str(text or "")}


def _client_reward(reward: dict) -> dict:
    # name must be "NoReward": the only RewardDefinition subclass registered
    # in the client's TypeHinting map — any other hint fails deserialization.
    return {
        "name": "NoReward",
        "rewardType": str(reward.get("rewardType") or "Tokens"),
        "rewardAmount": int(reward.get("rewardAmount") or 0),
        "flavor": str(reward.get("flavor") or ""),
    }


def _client_prize_table(prize_table: list) -> list:
    out = []
    for prize in prize_table or []:
        out.append({
            "start": int(prize.get("start") or 0),
            "end": int(prize.get("end") or 0),
            "rewards": [_client_reward(r) for r in prize.get("rewards") or []],
        })
    return out


# Legacy G.H feeType strings (client wallet sprites/checks key off these)
LEGACY_FEE_TYPES = {
    "coins": "Tokens", "tokens": "Tokens",
    "tickets": "TournamentTicket", "tournamentticket": "TournamentTicket",
    "gems": "Tokens",
}
LEGACY_FORMATS = ("Unlimited", "ThemeDeck", "Modified", "Expanded", "Legacy")


def _legacy_prizes(prize_table: list) -> list:
    """run.prizeTable rows -> legacy G.I[] (start/end are 1-based PLACES here)."""
    out = []
    for row in prize_table or []:
        for reward in row.get("rewards") or []:
            is_card = reward.get("rewardType") == "Archetype"
            out.append({
                "prizeType": {
                    "type": "Archetype" if is_card else "Tokens",
                    "archetypeID": str(reward.get("rewardProductID")) if is_card else None,
                },
                "amount": int(reward.get("rewardAmount") or 0),
                "startPlace": int(row.get("start") or 0),
                "endPlace": int(row.get("end") or 0),
            })
    return out


class TournamentDef:
    """Wraps one stored tournament row (definition_json + enabled)."""

    def __init__(self, tournament_id: str, definition: dict, enabled: bool):
        self.tournament_id = tournament_id
        self.definition = definition or {}
        self.enabled = enabled

    def _time(self, key: str, default: int) -> int:
        try:
            return int(self.definition.get(key) or default)
        except (TypeError, ValueError):
            return default

    @property
    def preview_time(self) -> int: return self._time("previewTime", 0)
    @property
    def start_time(self) -> int: return self._time("startTime", 0)
    @property
    def entry_closing_time(self) -> int: return self._time("entryClosingTime", FAR_FUTURE_MS)
    @property
    def resolution_time(self) -> int: return self._time("resolutionTime", FAR_FUTURE_MS)
    @property
    def disappear_time(self) -> int: return self._time("disappearTime", FAR_FUTURE_MS)

    @property
    def run_config(self) -> dict:
        return self.definition.get("run") or {}

    @property
    def leaderboard_config(self) -> dict:
        return self.definition.get("leaderboard") or {}

    def state(self, at_ms: int = None) -> str:
        now = now_ms() if at_ms is None else at_ms
        if now > self.disappear_time:
            return STATE_HIDDEN
        if now > self.resolution_time:
            return STATE_RESOLVED
        if now > self.entry_closing_time:
            return STATE_ENTRY_CLOSED
        if now > self.start_time:
            return STATE_OPEN
        if now > self.preview_time:
            return STATE_PREVIEW
        return STATE_BEFORE_PREVIEW

    def to_client_dict(self) -> dict:
        d = self.definition
        run = self.run_config
        lb = self.leaderboard_config
        game = d.get("game") or {}
        return {
            "id": self.tournament_id,
            "name": str(d.get("name") or "Tournament"),
            "title": _loc(d.get("title") or d.get("name") or "Tournament"),
            "description": _loc(d.get("description") or ""),
            "img": str(d.get("img") or ""),
            "background": str(d.get("background") or ""),
            "url": str(d.get("url") or ""),
            "previewTime": self.preview_time,
            "startTime": self.start_time,
            "entryClosingTime": self.entry_closing_time,
            "resolutionTime": self.resolution_time,
            "disappearTime": self.disappear_time,
            "maxRuns": int(d.get("maxRuns") or 0),
            "leaderboard": {
                "runs": int(lb.get("runs") or 0),
                "winValue": int(lb.get("winValue") or 3),
                "lossValue": int(lb.get("lossValue") or 0),
                "prizeTable": _client_prize_table(lb.get("prizeTable")),
            },
            "run": {
                "entryFee": [
                    {"currency": str(f.get("currency") or "Tokens"),
                     "amount": int(f.get("amount") or 0)}
                    for f in run.get("entryFee") or []
                ],
                "prizeTable": _client_prize_table(run.get("prizeTable")),
                "allowDeckSwitching": bool(run.get("allowDeckSwitching", True)),
                "maxWins": int(run.get("maxWins") or 0),
                "maxLosses": int(run.get("maxLosses") or 0),
                "maxGames": int(run.get("maxGames") or 0),
            },
            "active": bool(self.enabled),
            "game": {
                "format": game.get("format") or None,
                "matchStructure": str(game.get("matchStructure") or "SingleGame"),
                "strategy": str(game.get("strategy") or "Swiss"),
                "options": game.get("options") or {},
            },
            "limited": None,
            "league": None,
            "prizeBy": str(d.get("prizeBy") or "wins"),
        }

    @property
    def max_size(self) -> int:
        try:
            return int(self.definition.get("maxSize") or 8)
        except (TypeError, ValueError):
            return 8

    def legacy_entry_fees(self) -> list:
        """[{currency, amount}] rows the server actually charges (all of them)."""
        return [
            {"currency": str(f.get("currency") or "coins").lower(),
             "amount": int(f.get("amount") or 0)}
            for f in self.run_config.get("entryFee") or []
            if int(f.get("amount") or 0) > 0
        ]

    def to_legacy_dict(self) -> dict:
        """Legacy Events-scene entry (pie J.G.g). entryFee/prizes must be non-null
        arrays: three renderers deref them unguarded."""
        d = self.definition
        name = str(d.get("name") or "Tournament")
        desc_src = d.get("description") or ""
        desc = desc_src.get("id") if isinstance(desc_src, dict) else str(desc_src)
        return {
            "tournamentID": self.tournament_id,
            "name": name,
            "il8nName": None,
            "description": desc or "",
            "il8nDescription": None,
            "format": str(d.get("format") or "Unlimited"),
            "maxSize": self.max_size,
            "tournamentType": str(d.get("tournamentType") or "premiumTournament"),
            "matchStructure": str(d.get("matchStructure") or "SingleElimination"),
            "roundLength": int(d.get("roundLength") or 30),
            "delayBetweenRounds": int(d.get("delayBetweenRounds") or 10),
            "entryFee": [
                {"feeType": LEGACY_FEE_TYPES.get(f["currency"], "Tokens"),
                 "feeAmount": f["amount"]}
                for f in self.legacy_entry_fees()
            ],
            "prizes": _legacy_prizes(self.run_config.get("prizeTable")),
            "active": bool(self.enabled) and self.state() == STATE_OPEN,
        }


class TournamentManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TournamentManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.tournaments: List[TournamentDef] = []
        self.reload_from_db()

    def reload_from_db(self):
        try:
            from spirit.database import tournament_data
            rows = tournament_data.list_tournaments()
            self.tournaments = [
                TournamentDef(r["tournament_id"], r["definition"], r["enabled"])
                for r in rows
            ]
            logging.info(f"[Tournaments] Loaded {len(self.tournaments)} tournaments from DB")
        except Exception as e:
            logging.error(f"[Tournaments] Failed to load tournaments: {e}", exc_info=True)
            self.tournaments = []

    def get(self, tournament_id: str) -> Optional[TournamentDef]:
        wanted = (tournament_id or "").lower()
        for t in self.tournaments:
            if t.tournament_id.lower() == wanted:
                return t
        return None

    def visible_tournaments(self) -> List[TournamentDef]:
        """Enabled tournaments the client should still display."""
        now = now_ms()
        return [t for t in self.tournaments
                if t.enabled and t.state(now) != STATE_HIDDEN]


def validate_definition(definition: dict):
    """Sanity-checks an admin-supplied definition. Returns error text or None."""
    if not isinstance(definition, dict):
        return "definition must be an object"
    if not str(definition.get("name") or "").strip():
        return "name required"
    times = [definition.get(k) for k in
             ("previewTime", "startTime", "entryClosingTime", "resolutionTime", "disappearTime")]
    try:
        times = [int(t or 0) for t in times]
    except (TypeError, ValueError):
        return "times must be epoch milliseconds"
    stages = [t for t in times if t]
    if stages != sorted(stages):
        return "times must be in order: preview <= start <= entryClosing <= resolution <= disappear"
    try:
        max_size = int(definition.get("maxSize") or 8)
    except (TypeError, ValueError):
        return "maxSize must be a number"
    if max_size not in (2, 4, 8):
        return "maxSize must be 2, 4 or 8 (the bracket UI renders 8-player brackets)"
    if str(definition.get("matchStructure") or "SingleElimination") != "SingleElimination":
        return "only SingleElimination matchStructure is supported"
    fmt = definition.get("format")
    if fmt and str(fmt) not in LEGACY_FORMATS:
        return f"format must be one of {', '.join(LEGACY_FORMATS)}"
    run = definition.get("run") or {}
    if not any(int(run.get(k) or 0) > 0 for k in ("maxWins", "maxLosses", "maxGames")):
        return "run needs at least one of maxWins/maxLosses/maxGames > 0"
    for fee in run.get("entryFee") or []:
        from spirit.database.tournament_data import CURRENCY_FIELDS
        if str(fee.get("currency", "")).lower() not in CURRENCY_FIELDS:
            return f"unknown entry fee currency: {fee.get('currency')}"
        if int(fee.get("amount") or 0) < 0:
            return "entry fee amount must be >= 0"
    for table_owner in (run, definition.get("leaderboard") or {}):
        for prize in table_owner.get("prizeTable") or []:
            if int(prize.get("start") or 0) > int(prize.get("end") or 0):
                return "prize row start must be <= end"
            for r in prize.get("rewards") or []:
                rtype = r.get("rewardType")
                if rtype not in ("Tokens", "Archetype"):
                    return f"unsupported rewardType: {rtype} (use Tokens or Archetype)"
                if rtype == "Archetype" and not str(r.get("rewardProductID") or "").strip():
                    return "Archetype reward missing rewardProductID"
    return None
