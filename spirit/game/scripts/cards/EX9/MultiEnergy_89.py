"""STUB: effect not implemented — do not guess mechanics.
Multi Energy (EX9 #89): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Attach Multi Energy to 1 of your Pokémon. While in play, Multi Energy provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.) Multi Energy provides Colorless Energy when attached to a Pokémon that already has Special Energy cards attached to it.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8a514abf-635f-54a3-83ec-7f0ef5585be4",
    key="EX9",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=89,
    set_code="EX9",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
