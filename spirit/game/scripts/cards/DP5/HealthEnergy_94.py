"""STUB: effect not implemented — do not guess mechanics.
Health Energy (DP5 #94): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Health Energy provides Colorless Energy. When you attach this card from your hand to 1 of your Pokémon, remove 1 damage counter from that Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="972c2e95-aabc-569f-b109-2c1af9875f55",
    key="DP5",
    name="Health Energy",
    display_name="Health Energy",
    searchable_by=["Health Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
