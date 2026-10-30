"""STUB: effect not implemented — do not guess mechanics.
Recycle Energy (NEO1 #105): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Recycle Energy provides Colorless Energy. (Doesn't count as a basic Energy card.)
  - If this card is put into your discard pile from play, return it to your hand.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ad1a7ee4-285b-539f-8a50-c264a88bb858",
    key="NEO1",
    name="Recycle Energy",
    display_name="Recycle Energy",
    searchable_by=["Recycle Energy", "Special"],
    subtypes=["Special"],
    collector_number=105,
    set_code="NEO1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
