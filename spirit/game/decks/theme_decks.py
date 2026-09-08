"""Card references and immutable indexes for scripted deck products."""

import uuid
from collections import Counter, defaultdict
from dataclasses import dataclass
from types import MappingProxyType

from spirit.game.attributes import AttrID


@dataclass(frozen=True)
class DeckEntry:
    card: str
    count: int = 1

    def __post_init__(self):
        if not isinstance(self.card, str) or not self.card.strip():
            raise ValueError("DeckEntry.card must be a card GUID or SET/number reference")
        if type(self.count) is not int or not 1 <= self.count <= 60:
            raise ValueError(f"{self.card}: count must be an integer from 1 to 60")


class CardReferenceResolver:
    """Indexes one loaded card catalog for unambiguous reference resolution."""

    def __init__(self, card_registry):
        self.cards = card_registry.cards
        self.cards_by_guid = {card.guid.lower(): card for card in self.cards}
        self._by_number = defaultdict(set)
        for card in self.cards:
            number = str(card.get_attribute_value(AttrID.COLLECTOR_NUMBER)).casefold()
            self._by_number[(card.key.casefold(), number)].add(card.guid.lower())

    def resolve(self, reference):
        ref = reference.strip()
        if "/" in ref:
            key, number = (part.strip().casefold() for part in ref.split("/", 1))
            matches = self._by_number.get((key, number), set())
            if len(matches) > 1:
                raise ValueError(f"Ambiguous card reference {reference!r}; use its GUID")
            if matches:
                return next(iter(matches))
        else:
            try:
                guid = str(uuid.UUID(ref))
            except ValueError:
                guid = ""
            if guid in self.cards_by_guid:
                return guid
        raise ValueError(f"Unknown card reference {reference!r}")


def deck_signature(card_guids):
    return tuple(sorted(Counter(str(guid).lower() for guid in card_guids).items()))


class ThemeDeckRegistry:
    """An atomically replaceable catalog with quantity-aware deck matching."""

    def __init__(self, products=()):
        decks = {p.guid: p for p in products if getattr(p, "contents", ())}
        self._decks = MappingProxyType(decks)
        self._contents = MappingProxyType({key: tuple(p.contents) for key, p in decks.items()})
        signatures = {}
        legal_cards = set()
        for product in decks.values():
            if product.is_theme_deck and product.theme_legal:
                signatures.setdefault(deck_signature(product.contents), product)
                legal_cards.update(product.contents)
        self._signatures = MappingProxyType(signatures)
        self.legal_cards = frozenset(legal_cards)

    def get(self, product_guid):
        return self._decks.get(str(product_guid).lower())

    def contents_map(self):
        return {key: list(contents) for key, contents in self._contents.items()}

    def match_deck(self, card_guids):
        return self._signatures.get(deck_signature(card_guids))


class ThemeDeckCatalog:
    """Stable reference to the last successfully published registry."""

    def __init__(self):
        self.registry = ThemeDeckRegistry()

    def get(self, product_guid):
        return self.registry.get(product_guid)

    def contents_map(self):
        return self.registry.contents_map()

    def match_deck(self, card_guids):
        return self.registry.match_deck(card_guids)


theme_decks = ThemeDeckCatalog()
