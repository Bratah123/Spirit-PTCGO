import json
import logging
import os
import time
from typing import Any, Dict, List, Optional, Set, Tuple

from spirit.game.attributes import AttrID, CardType, DeckFormat
from spirit.game.models.formats import GameFormat, FORMAT_WIRE_NAMES
from spirit.game.set_utils import card_script_counts
from spirit.game.scripts.cards import loader as card_loader

FORMATS_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'database', 'json_data', 'formats.json'
))

LEGACY_SETS = {"BW1"}
STANDARD_NON_SWSH_SETS = {"CEL25", "PGO", "CZ", "CUSTOM", "Free_Energy"}


def is_basic_energy_card(card) -> bool:
    ct = card.get_attribute_value(AttrID.CARD_TYPE)
    if ct != CardType.ENERGY.value:
        return False
    return not card.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)


def _default_formats() -> List[GameFormat]:
    """All loaded sets -> Expanded/Unlimited, SWSH block -> Standard, BW -> Legacy."""
    loaded = sorted(card_script_counts().keys())
    standard = [s for s in loaded if s.startswith("SWSH") or s in STANDARD_NON_SWSH_SETS]
    legacy = [s for s in loaded if s in LEGACY_SETS or s in ("Free_Energy", "CUSTOM")]
    return [
        GameFormat("Standard", DeckFormat.STANDARD.value, "Modified", sets=standard),
        GameFormat("Expanded", DeckFormat.EXPANDED.value, "Expanded", sets=loaded),
        GameFormat("Legacy", DeckFormat.LEGACY.value, "Legacy", sets=legacy),
        GameFormat("Unlimited", DeckFormat.UNLIMITED.value, "Unlimited", all_sets=True),
    ]


def validate_formats(data: Any) -> Tuple[Optional[List[dict]], Optional[str]]:
    """Round-trips a formats payload; returns (normalized list, None) or (None, error)."""
    if not isinstance(data, list) or not data:
        return None, "'formats' must be a non-empty list"
    normalized, seen_guids, seen_keys = [], set(), set()
    known_sets = set(card_script_counts().keys())
    for entry in data:
        try:
            fmt = GameFormat.from_dict(entry)
        except (ValueError, TypeError) as e:
            return None, str(e)
        if fmt.guid in seen_guids:
            return None, f"duplicate format guid {fmt.guid}"
        if fmt.key in seen_keys:
            return None, f"duplicate format key {fmt.key}"
        seen_guids.add(fmt.guid)
        seen_keys.add(fmt.key)
        for s in fmt.sets:
            if s not in known_sets:
                logging.warning(f"[Formats] Format '{fmt.key}' lists unknown set '{s}'")
        normalized.append(fmt.to_dict())
    return normalized, None


class FormatManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FormatManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.formats: List[GameFormat] = []
        self._by_guid: Dict[str, GameFormat] = {}
        self._ref_cache: Dict[str, Tuple[Set[str], Set[str]]] = {}
        self._ref_cache_stamp = -1
        self.load_formats()

    def load_formats(self):
        self._ref_cache.clear()
        self._ref_cache_stamp = -1
        if os.path.exists(FORMATS_PATH):
            try:
                with open(FORMATS_PATH, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.formats = [GameFormat.from_dict(e) for e in data.get("formats", [])]
                if not self.formats:
                    raise ValueError("formats.json contains no formats")
                logging.info(f"[Formats] Loaded {len(self.formats)} formats from {FORMATS_PATH}")
            except (OSError, ValueError, TypeError, json.JSONDecodeError) as e:
                logging.error(f"[Formats] Failed to load formats.json, using defaults: {e}")
                self.formats = _default_formats()
        else:
            self.formats = _default_formats()
            try:
                with open(FORMATS_PATH, 'w', encoding='utf-8') as f:
                    json.dump({"formats": [fmt.to_dict() for fmt in self.formats]}, f, indent=2)
                logging.info(f"[Formats] Wrote default formats.json to {FORMATS_PATH}")
            except OSError as e:
                logging.error(f"[Formats] Could not write default formats.json: {e}")
        self._by_guid = {fmt.guid: fmt for fmt in self.formats}

    def by_guid(self, format_guid: str) -> Optional[GameFormat]:
        return self._by_guid.get((format_guid or "").lower())

    def format_name(self, format_guid: str) -> str:
        fmt = self.by_guid(format_guid)
        if fmt:
            return fmt.format_name
        return FORMAT_WIRE_NAMES.get((format_guid or "").lower(), "Modified")

    def play_format_guids(self) -> List[str]:
        return [fmt.guid for fmt in self.formats]

    def legal_format_guids_for_set(self, set_code: str) -> List[str]:
        return [fmt.guid for fmt in self.formats if fmt.allows_set(set_code)]

    def _resolve_card_ref(self, ref: str) -> Optional[str]:
        if "/" in ref:
            set_code, _, num = ref.partition("/")
            for c in card_loader.cards:
                if c.key.upper() == set_code.upper() and \
                        str(c.get_attribute_value(AttrID.COLLECTOR_NUMBER)) == num.strip():
                    return c.guid.lower()
            logging.warning(f"[Formats] Card ref '{ref}' matched no loaded card")
            return None
        return ref.lower()

    def _resolved_refs(self, fmt: GameFormat) -> Tuple[Set[str], Set[str]]:
        # "SET/num" refs need the card scripts; re-resolve if the loader reloaded.
        if self._ref_cache_stamp != len(card_loader.cards):
            self._ref_cache.clear()
            self._ref_cache_stamp = len(card_loader.cards)
        cached = self._ref_cache.get(fmt.guid)
        if cached is None:
            banned = {g for g in map(self._resolve_card_ref, fmt.banned_cards) if g}
            extra = {g for g in map(self._resolve_card_ref, fmt.extra_legal_cards) if g}
            cached = (banned, extra)
            self._ref_cache[fmt.guid] = cached
        return cached

    def is_card_eventually_legal(self, format_guid: str, card) -> bool:
        """Legality ignoring any legalFrom time gate (the formatLegality bool slot)."""
        fmt = self.by_guid(format_guid)
        if fmt is None:
            return False
        if is_basic_energy_card(card):
            return True
        banned, extra = self._resolved_refs(fmt)
        guid = card.guid.lower()
        if guid in banned:
            return False
        if guid in extra:
            return True
        set_code = card.get_attribute_value(AttrID.SET_KEY) or card.key
        return fmt.allows_set(set_code)

    def is_card_legal(self, format_guid: str, card, now_ms: Optional[int] = None) -> bool:
        if not self.is_card_eventually_legal(format_guid, card):
            return False
        start = self.legal_time_ms(format_guid, card)
        return start <= (now_ms if now_ms is not None else int(time.time() * 1000))

    def legal_time_ms(self, format_guid: str, card) -> int:
        fmt = self.by_guid(format_guid)
        if fmt is None:
            return 0
        set_code = card.get_attribute_value(AttrID.SET_KEY) or card.key
        return fmt.legal_from.get(set_code, 0)
