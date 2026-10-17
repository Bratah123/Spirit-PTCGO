"""STUB: effect not implemented — do not guess mechanics.
Double Colorless Energy (XY1 #130): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Double Colorless Energy provides ColorlessColorless Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5c47616e-2e51-5bc9-90ab-7d41fe54b681",
    key="XY1",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=130,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
