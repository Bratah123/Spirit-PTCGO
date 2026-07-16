import uuid
from typing import Any, Dict, List, Optional

from spirit.game.attributes import DeckFormat

# Client hashes these exact strings in DeckValidationManager.updateValidations
# and the attr-10860 local path; "Standard" is called "Modified" on the wire.
FORMAT_WIRE_NAMES = {
    DeckFormat.STANDARD.value: "Modified",
    DeckFormat.EXPANDED.value: "Expanded",
    DeckFormat.UNLIMITED.value: "Unlimited",
    DeckFormat.LEGACY.value: "Legacy",
    DeckFormat.THEME.value: "ThemeDeck",
    DeckFormat.TRAINER_CHALLENGE.value: "TrainerChallenge",
}


class GameFormat:
    """One play format: the sets and per-card exceptions that are legal in it."""

    def __init__(
        self,
        key: str,
        guid: str,
        format_name: str,
        sets: Optional[List[str]] = None,
        all_sets: bool = False,
        banned_cards: Optional[List[str]] = None,
        extra_legal_cards: Optional[List[str]] = None,
        legal_from: Optional[Dict[str, int]] = None,
    ):
        self.key = key
        self.guid = str(guid).lower()
        self.format_name = format_name
        self.sets = list(sets or [])
        self.all_sets = bool(all_sets)
        # Card refs: bare archetype GUID or "SETCODE/collector_number".
        self.banned_cards = [str(c) for c in (banned_cards or [])]
        self.extra_legal_cards = [str(c) for c in (extra_legal_cards or [])]
        # set_code -> epoch ms when the set becomes legal (0/absent = always).
        self.legal_from = {str(k): int(v) for k, v in (legal_from or {}).items()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GameFormat":
        key = data.get("key")
        guid = data.get("guid")
        if not key or not isinstance(key, str):
            raise ValueError("format entry needs a non-empty 'key'")
        if not guid:
            raise ValueError(f"format '{key}' needs a 'guid'")
        uuid.UUID(str(guid))
        sets = data.get("sets", [])
        if not isinstance(sets, list) or not all(isinstance(s, str) for s in sets):
            raise ValueError(f"format '{key}': 'sets' must be a list of set codes")
        for field in ("bannedCards", "extraLegalCards"):
            refs = data.get(field, [])
            if not isinstance(refs, list) or not all(isinstance(r, str) for r in refs):
                raise ValueError(f"format '{key}': '{field}' must be a list of card refs")
        legal_from = data.get("legalFrom", {})
        if not isinstance(legal_from, dict):
            raise ValueError(f"format '{key}': 'legalFrom' must be an object")
        return cls(
            key=key,
            guid=str(guid),
            format_name=data.get("formatName") or FORMAT_WIRE_NAMES.get(str(guid).lower(), key),
            sets=sets,
            all_sets=bool(data.get("allSets", False)),
            banned_cards=data.get("bannedCards", []),
            extra_legal_cards=data.get("extraLegalCards", []),
            legal_from=legal_from,
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "key": self.key,
            "guid": self.guid,
            "formatName": self.format_name,
            "sets": list(self.sets),
            "allSets": self.all_sets,
            "bannedCards": list(self.banned_cards),
            "extraLegalCards": list(self.extra_legal_cards),
            "legalFrom": dict(self.legal_from),
        }

    def allows_set(self, set_code: Optional[str]) -> bool:
        return self.all_sets or (set_code in self.sets)
