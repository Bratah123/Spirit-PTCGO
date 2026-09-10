"""Deferred printing definitions resolved by the card script loader."""

from copy import deepcopy
import json
from pathlib import PurePosixPath
from typing import List, Optional
import uuid

from spirit.game.attributes import AttrID
from spirit.game.content.definitions import (
    ABILITIES_BY_ID, CARD_DEFS_BY_GUID, TRAINER_EFFECTS_BY_GUID,
    CardDefinition, PokemonCardDef, TrainerCardDef, EnergyCardDef,
    Foil, ability_id_for, unimplemented,
)


class ReprintCardDef:
    """Declare printing metadata while inheriting all gameplay from a script."""

    parent_type = CardDefinition

    def __init__(
        self, *, inherits: str, guid: str, key: str, set_code: str,
        collector_number: int, rarity: int,
        display_name: Optional[str] = None,
        searchable_by: Optional[List[str]] = None,
        image_url: Optional[str] = None,
        image_name: Optional[str] = None,
        foil: Optional[Foil] = None,
    ):
        path = PurePosixPath(inherits)
        if (not inherits or "\\" in inherits or path.is_absolute()
                or ".." in path.parts or path.suffix or ":" in inherits
                or str(path) != inherits):
            raise ValueError("inherits must be a scripts-relative path without .py")
        self.inherits = inherits
        self.guid = str(uuid.UUID(guid))
        self.key = key
        self.set_code = set_code
        self.collector_number = collector_number
        self.rarity = rarity
        self.display_name = display_name
        self.searchable_by = searchable_by
        self.image_url = image_url
        self.image_name = image_name
        self.foil = foil

    def resolve(self, parent: CardDefinition) -> CardDefinition:
        """Copy gameplay, rebuild printing attributes, and register fresh IDs."""
        if not isinstance(parent, self.parent_type):
            raise TypeError(f"{self.inherits}: expected {self.parent_type.__name__}, "
                            f"got {type(parent).__name__}")
        if self.guid.lower() == parent.guid.lower():
            raise ValueError("A reprint must have its own GUID")
        card = deepcopy(parent, {id(unimplemented): unimplemented})
        for field in ("guid", "key", "set_code", "collector_number", "rarity"):
            setattr(card, field, getattr(self, field))
        for field in ("display_name", "searchable_by"):
            if getattr(self, field) is not None:
                setattr(card, field, deepcopy(getattr(self, field)))
        attrs = card.extra_attributes
        for attr in (
            AttrID.SET_KEY, AttrID.SET_CACHE_KEY, AttrID.COLLECTOR_NUMBER,
            AttrID.RARITY, AttrID.COLLECTION_ID, AttrID.IMAGE_URL, AttrID.IMAGE_NAME,
            AttrID.FOIL_MASK, AttrID.FOIL_EFFECT, AttrID.FOIL_EFFECTS,
            AttrID.FOIL_INTENSITY,
        ):
            attrs.pop(str(attr.value), None)
        for attr, value in ((AttrID.IMAGE_URL, self.image_url),
                            (AttrID.IMAGE_NAME, self.image_name)):
            if value is not None:
                attrs[str(attr.value)] = {"type": "string", "value": value}
        card.foil = deepcopy(self.foil)
        if card.foil is not None:
            attrs.update(card.foil.to_attributes())

        abilities = getattr(card, "abilities", [])
        offset = 100 if isinstance(card, TrainerCardDef) else 0
        bindings = [(a, slot + offset) for slot, a in enumerate(abilities)]
        if getattr(card, "ability", None) is not None:
            bindings.append((card.ability, 0))
        bindings.extend((a, slot) for slot, a in
                        enumerate(getattr(card, "granted_abilities", [])))
        for ability, slot in bindings:
            ability.ability_id = ability_id_for(card.guid, slot)
        if str(AttrID.PIE_ABILITIES.value) in attrs:
            attrs[str(AttrID.PIE_ABILITIES.value)] = {
                "type": "json", "value": json.dumps([a.to_dict() for a in abilities]),
            }
        for ability, _ in bindings:
            ABILITIES_BY_ID[ability.ability_id] = ability
        if isinstance(card, TrainerCardDef) and card.effect is not None:
            TRAINER_EFFECTS_BY_GUID[card.guid.lower()] = card.effect
        CARD_DEFS_BY_GUID[card.guid.lower()] = card
        return card


class PokemonReprintCardDef(ReprintCardDef):
    """A printing of a Pokemon card with identical gameplay."""

    parent_type = PokemonCardDef


class TrainerReprintCardDef(ReprintCardDef):
    """A printing of an Item, Supporter, Stadium, or Pokemon Tool."""

    parent_type = TrainerCardDef


class EnergyReprintCardDef(ReprintCardDef):
    """A printing of a basic or special Energy card."""

    parent_type = EnergyCardDef
