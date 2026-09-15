"""Physical LEGEND printings and their runtime-only combined Pokemon."""

from enum import Enum
import json
from pathlib import PurePosixPath
from typing import List, Optional

from spirit.game.attributes import AttrID, CardType, PokemonStage, PokemonTypes
from spirit.game.content.definitions import CardDefinition, PokemonCardDef, def_for


class LegendHalf(str, Enum):
    TOP = "top"
    BOTTOM = "bottom"


def _validate_static_attributes(attributes):
    """Match entity references belong on assembled entities, never archetypes."""
    references = {str(AttrID.LEGEND_TOP_HALF.value), str(AttrID.LEGEND_BOTTOM_HALF.value)}
    if any(str(key) in references for key in (attributes or {})):
        raise ValueError("LEGEND half entity IDs are assigned at runtime by assemble_legend")


class LegendPokemonDef(PokemonCardDef):
    """The card that shows up in play when both halves are combined, this shouldn't show up in collections
        like a normal pokemon card would."""

    runtime_only = True

    def __init__(self, *, prize_count: int = 1, **kwargs):
        if type(prize_count) is not int or prize_count not in (1, 2):
            raise ValueError("LEGEND prize_count must be 1 or 2")
        _validate_static_attributes(kwargs.get("attributes"))
        kwargs["stage"] = PokemonStage.LEGEND
        kwargs["unplayable_from_hand"] = True
        super().__init__(**kwargs)
        self.prize_count = prize_count
        self.extra_attributes[str(AttrID.IS_LEGEND.value)] = {"type": "bool", "value": True}


class LegendHalfCardDef(CardDefinition):
    """A collectible half referencing a combined definition by script path."""

    def __init__(self, *, legend: str, half: LegendHalf,
                 hp: Optional[int] = None, elements: Optional[List[PokemonTypes]] = None, **kwargs):
        _validate_static_attributes(kwargs.get("attributes"))
        path = PurePosixPath(legend)
        if (not legend or "\\" in legend or path.is_absolute() or ".." in path.parts
                or path.suffix or ":" in legend or str(path) != legend):
            raise ValueError("legend must be a scripts-relative path without .py")
        self.half = LegendHalf(half)
        self.legend = legend
        self.legend_definition = None
        super().__init__(**kwargs)
        self.extra_attributes.update({
            str(AttrID.CARD_TYPE.value): {"type": "int", "value": CardType.LEGEND_HALF.value},
            str(AttrID.STAGE.value): {"type": "int", "value": PokemonStage.LEGEND.value},
            str(AttrID.IS_LEGEND.value): {"type": "bool", "value": True},
            str(AttrID.PIE_ABILITIES.value): {"type": "json", "value": "[]"},
        })
        if hp is not None:
            self.extra_attributes[str(AttrID.HP.value)] = {"type": "int", "value": hp}
        if elements is not None:
            self.extra_attributes[str(AttrID.POKEMON_TYPES.value)] = {
                "type": "json", "value": json.dumps([element.value for element in elements]),
            }

    def resolve_legend(self, definition):
        """Bind a validated pair while preserving this printing's artwork."""
        if not isinstance(definition, LegendPokemonDef):
            raise TypeError(f"{self.legend}: expected LegendPokemonDef")
        if self.name != definition.name:
            raise ValueError("Both LEGEND halves must use the combined Pokemon's name")
        if self.guid.lower() == definition.guid.lower():
            raise ValueError("A LEGEND half must have its own GUID")
        self.legend_definition = definition


def matching_legend_halves(first, second) -> bool:
    """Whether two physical copies belong to opposite halves of one LEGEND."""
    a, b = def_for(first.archetype_id), def_for(second.archetype_id)
    return (first is not second and isinstance(a, LegendHalfCardDef)
            and isinstance(b, LegendHalfCardDef) and a.legend_definition is not None
            and a.legend_definition is b.legend_definition and a.half != b.half)
