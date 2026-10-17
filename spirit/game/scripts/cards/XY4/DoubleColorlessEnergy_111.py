"""STUB: effect not implemented — do not guess mechanics.
Double Colorless Energy (XY4 #111): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Double Colorless Energy provides ColorlessColorless Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="30bf569c-5189-52c4-8a9f-bd63977f9634",
    key="XY4",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=111,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
