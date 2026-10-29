"""STUB: effect not implemented — do not guess mechanics.
Rainbow Energy (SM7 #151): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy. While in play, this card provides every type of Energy but provides only 1 Energy at a time. When you attach this card from your hand to 1 of your Pokémon, put 1 damage counter on that Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="1b7d9152-2b27-5cc0-9905-a43e7c5df3f6",
    key="SM7",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=151,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
