import json
import logging
from typing import Any, Dict, List, Optional

from spirit.game.attributes import AttrID, CardType, PokemonStage
from spirit.game.format_manager import FormatManager, is_basic_energy_card
from spirit.game.scripts.cards import loader as card_loader

DECK_SIZE = 60
MAX_COPIES = 4


def _detail(failure_type: str, text: str, offenders: Optional[List[str]] = None) -> Dict[str, Any]:
    # failureType coerces by enum member name; explanation renders verbatim for unknown loc keys
    return {
        "explanation": {"id": text},
        "failureType": failure_type,
        "offendingArchetypeIDs": offenders or [],
        "additionalData": None,
    }


def card_display_name(card) -> str:
    if card.display_name:
        return card.display_name
    name_val = card.get_attribute_value(AttrID.NAME)
    if isinstance(name_val, str) and name_val.startswith('{'):
        try:
            return json.loads(name_val).get("id") or card.guid
        except (ValueError, AttributeError):
            return name_val
    return str(name_val) if name_val else card.guid


def _is_basic_pokemon_card(card) -> bool:
    return (
        card.get_attribute_value(AttrID.CARD_TYPE) == CardType.POKEMON.value
        and card.get_attribute_value(AttrID.STAGE, PokemonStage.BASIC.value) == PokemonStage.BASIC.value
    )


class DeckValidator:
    """Validates one deck against the deck-building rules and any number of formats."""

    def __init__(self, deck_dict: Dict[str, Any], owned_counts: Optional[Dict[str, int]] = None):
        self.deck_id = deck_dict.get("deckID")
        self.deck_name = deck_dict.get("deckName", "Unknown Deck")
        piles = deck_dict.get("piles") or {}
        pile_cards = piles.get("deck") or piles.get("CakePile") or []
        self.guids: List[str] = [str(g).lower() for g in pile_cards]
        self.owned_counts = owned_counts
        self.manager = FormatManager()
        if not card_loader.cards:
            card_loader.load_all()
        self.cards = []
        self.unknown_guids: List[str] = []
        for guid in self.guids:
            card = card_loader.cards_by_guid.get(guid)
            if card is None:
                self.unknown_guids.append(guid)
            else:
                self.cards.append(card)
        self._base_details: Optional[List[dict]] = None

    def _base_failures(self) -> List[dict]:
        """Format-independent rule failures, computed once per deck."""
        if self._base_details is not None:
            return self._base_details
        details = []

        if len(self.guids) != DECK_SIZE:
            details.append(_detail(
                "ExactSize",
                f"A deck must contain exactly {DECK_SIZE} cards (this deck has {len(self.guids)})."))

        if self.unknown_guids:
            details.append(_detail(
                "MustNotContain",
                "This deck contains cards unknown to the server.",
                sorted(set(self.unknown_guids))))

        by_name: Dict[str, List[str]] = {}
        for card in self.cards:
            if is_basic_energy_card(card):
                continue
            by_name.setdefault(card_display_name(card), []).append(card.guid.lower())
        over_limit = {name: guids for name, guids in by_name.items() if len(guids) > MAX_COPIES}
        if over_limit:
            names = ", ".join(sorted(over_limit))
            offenders = sorted({g for guids in over_limit.values() for g in guids})
            details.append(_detail(
                "MaxDuplicates",
                f"A deck can't contain more than {MAX_COPIES} cards with the same name: {names}.",
                offenders))

        if not any(_is_basic_pokemon_card(c) for c in self.cards):
            details.append(_detail(
                "MustContain",
                "A deck must contain at least 1 Basic Pokémon."))

        if self.owned_counts is not None:
            counts: Dict[str, int] = {}
            for card in self.cards:
                if is_basic_energy_card(card):
                    continue
                counts[card.guid.lower()] = counts.get(card.guid.lower(), 0) + 1
            unowned = sorted(g for g, n in counts.items() if self.owned_counts.get(g, 0) < n)
            if unowned:
                details.append(_detail(
                    "UnownedCards",
                    "This deck contains cards you don't own.",
                    unowned))

        self._base_details = details
        return details

    def validate(self, format_guids: List[str]) -> List[dict]:
        """One DeckValidationResult row per requested format."""
        rows = []
        base = self._base_failures()
        for fmt_guid in format_guids:
            fmt_guid = str(fmt_guid).lower()
            details = list(base)
            fmt = self.manager.by_guid(fmt_guid)
            if fmt is None:
                details.append(_detail(
                    "BoolRestriction",
                    f"The {self.manager.format_name(fmt_guid)} format is not available on this server."))
            else:
                offenders = sorted({
                    card.guid.lower() for card in self.cards
                    if not self.manager.is_card_legal(fmt_guid, card)})
                if offenders:
                    details.append(_detail(
                        "DeckContainsBannedCards",
                        f"This deck contains cards that are not legal in the {fmt.format_name} format.",
                        offenders))
            rows.append({
                "deckID": self.deck_id,
                "format": fmt_guid,
                "formatName": self.manager.format_name(fmt_guid),
                "valid": not details,
                "results": details,
            })
        return rows

    def valid_format_names(self) -> List[str]:
        """Format wire-names this deck fully passes — the deck attr 10860 payload."""
        return [row["formatName"] for row in self.validate(self.manager.play_format_guids())
                if row["valid"]]


def validate_deck(deck_dict: Dict[str, Any], format_guids: Optional[List[str]] = None,
                  owned_counts: Optional[Dict[str, int]] = None) -> List[dict]:
    validator = DeckValidator(deck_dict, owned_counts=owned_counts)
    if format_guids is None:
        format_guids = validator.manager.play_format_guids()
    results = validator.validate(format_guids)
    invalid = [r["formatName"] for r in results if not r["valid"]]
    logging.info(
        f"[Rules] Validated deck '{validator.deck_name}' ({validator.deck_id}): "
        f"{'all formats OK' if not invalid else 'invalid in ' + ', '.join(invalid)}")
    return results


def valid_format_names(deck_dict: Dict[str, Any],
                       owned_counts: Optional[Dict[str, int]] = None) -> List[str]:
    return DeckValidator(deck_dict, owned_counts=owned_counts).valid_format_names()
