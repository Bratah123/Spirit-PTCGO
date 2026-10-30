"""STUB: effect not implemented — do not guess mechanics.
Rainbow Energy (EX1 #95): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Attach Rainbow Energy to 1 of your Pokémon. While in play, Rainbow Energy provides every type of Energy but provides only 1 Energy at a time. (Doesn't count as a basic Energy card when not in play.) When you attach this card from your hand to 1 of your Pokémon, put 1 damage counter on that Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7b8107fd-3152-5d6e-b442-f47dc092b256",
    key="EX1",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX1",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
