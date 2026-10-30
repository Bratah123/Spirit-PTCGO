"""STUB: effect not implemented — do not guess mechanics.
Cyclone Energy (DP7 #94): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Cyclone Energy provides Colorless Energy. When you attach this card from your hand to your Active Pokémon, switch 1 of the Defending Pokémon with 1 of your opponent's Benched Pokémon. Your opponent chooses the Benched Pokémon to switch.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ed1ae23e-df29-52ec-8303-76ce2738e1d2",
    key="DP7",
    name="Cyclone Energy",
    display_name="Cyclone Energy",
    searchable_by=["Cyclone Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
