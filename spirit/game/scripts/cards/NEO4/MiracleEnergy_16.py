"""STUB: effect not implemented — do not guess mechanics.
Miracle Energy (NEO4 #16): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - You can't have more than 1 Miracle Energy in your deck. Attach Miracle Energy to 1 of your Shining or Light Pokémon. At the end of your turn, discard Miracle Energy.
While in play, Miracle Energy counts as every type of Energy but provides only 2 Energy at a time.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8ee9e2f6-2010-5cd1-b830-f9721f632b60",
    key="NEO4",
    name="Miracle Energy",
    display_name="Miracle Energy",
    searchable_by=["Miracle Energy", "Special"],
    subtypes=["Special"],
    collector_number=16,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
