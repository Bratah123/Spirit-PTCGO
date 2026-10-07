"""Physical V-UNION pieces and their runtime-only combined Pokemon."""

from enum import IntEnum
import json
from typing import List, Optional

from spirit.game.attributes import AbilityTypes, AttrID, CardType, PokemonStage, PokemonTypes
from spirit.game.content.definitions import (
    Ability, CardDefinition, PokemonCardDef, ability_id_for, def_for, validate_script_reference,
)

VUNION_SUBTYPE = "V-UNION"
# Label of the discard-pile panel button that summons the V-UNION.
ASSEMBLE_TITLE = "V-UNION"
ASSEMBLE_TEXT = ("Once per game during your turn, combine 4 different {name} "
                 "from your discard pile and put them onto your Bench.")


class VUnionPiece(IntEnum):
    """Where a piece sits in the assembled card; the order is the client's CardSlot1-4 / Subcard0-3."""
    TOP_LEFT = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = 2
    BOTTOM_RIGHT = 3


def _with_vunion_subtype(subtypes) -> List[str]:
    subtypes = list(subtypes or [])
    if VUNION_SUBTYPE not in subtypes:
        subtypes.append(VUNION_SUBTYPE)
    return subtypes


class VUnionPokemonDef(PokemonCardDef):
    """The Pokemon that enters play once all four pieces combine; never collectible on its own.

    `image_name` is the combined art's asset name, defaulting to the original
    client's "{first}to{last}" piece-number convention (e.g. "159to162").
    """

    runtime_only = True

    def __init__(self, *, image_name: Optional[str] = None, **kwargs):
        kwargs["stage"] = PokemonStage.VUNION
        kwargs["unplayable_from_hand"] = True
        kwargs["subtypes"] = _with_vunion_subtype(kwargs.get("subtypes"))
        super().__init__(**kwargs)
        self.image_name = image_name
        self.pieces: List["VUnionPieceCardDef"] = []

    def bind_pieces(self, pieces: List["VUnionPieceCardDef"]):
        """Attach the four resolved printings, ordered by board position."""
        self.pieces = sorted(pieces, key=lambda piece: piece.piece)
        if self.image_name is None:
            self.image_name = f"{self.pieces[0].collector_number}to{self.pieces[-1].collector_number}"

    def assemble_text(self) -> str:
        return ASSEMBLE_TEXT.format(name=self.display_name or "V-UNION")


class VUnionPieceCardDef(CardDefinition):
    """A collectible quarter of a V-UNION, referencing its combined definition by script path."""

    def __init__(self, *, vunion: str, piece: VUnionPiece,
                 hp: Optional[int] = None, elements: Optional[List[PokemonTypes]] = None, **kwargs):
        validate_script_reference(vunion, "vunion")
        self.piece = VUnionPiece(piece)
        self.vunion = vunion
        self.vunion_definition: Optional[VUnionPokemonDef] = None
        kwargs["subtypes"] = _with_vunion_subtype(kwargs.get("subtypes"))
        super().__init__(**kwargs)
        # The summon is a dedicated action, so this ability is display-only (never in ABILITIES_BY_ID).
        self.assemble_ability = Ability(ASSEMBLE_TITLE, ability_type=AbilityTypes.POKE_ABILITY)
        self.assemble_ability.ability_id = ability_id_for(self.guid, 0)
        self.extra_attributes.update({
            # LegendHalf is the client's only non-Pokemon card type its discard click handler accepts.
            str(AttrID.CARD_TYPE.value): {"type": "int", "value": CardType.LEGEND_HALF.value},
            str(AttrID.STAGE.value): {"type": "int", "value": PokemonStage.VUNION.value},
            str(AttrID.PIE_ABILITIES.value): {"type": "json", "value": "[]"},
        })
        if hp is not None:
            self.extra_attributes[str(AttrID.HP.value)] = {"type": "int", "value": hp}
        self._elements = elements
        if elements is not None:
            self._set_elements(elements)

    def _set_elements(self, elements: List[PokemonTypes]):
        self.extra_attributes[str(AttrID.POKEMON_TYPES.value)] = {
            "type": "json", "value": json.dumps([getattr(e, "value", e) for e in elements]),
        }

    def resolve_vunion(self, definition):
        """Bind this printing to its combined Pokemon; the panel button text needs the combined name."""
        if not isinstance(definition, VUnionPokemonDef):
            raise TypeError(f"{self.vunion}: expected VUnionPokemonDef")
        if self.name != definition.name:
            raise ValueError("Every V-UNION piece must use the combined Pokemon's name")
        if self.guid.lower() == definition.guid.lower():
            raise ValueError("A V-UNION piece must have its own GUID")
        self.vunion_definition = definition
        if self._elements is None:
            types = definition.extra_attributes.get(str(AttrID.POKEMON_TYPES.value))
            if types is not None:
                self.extra_attributes[str(AttrID.POKEMON_TYPES.value)] = dict(types)
        self.assemble_ability.game_text = definition.assemble_text()
        self.extra_attributes[str(AttrID.PIE_ABILITIES.value)] = {
            "type": "json", "value": json.dumps([self.assemble_ability.to_dict()]),
        }


def piece_definition(card) -> Optional[VUnionPieceCardDef]:
    """The bound piece definition behind a card entity, if it is a playable V-UNION piece."""
    definition = def_for(getattr(card, "archetype_id", None))
    if isinstance(definition, VUnionPieceCardDef) and definition.vunion_definition is not None:
        return definition
    return None
