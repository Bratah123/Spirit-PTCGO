"""STUB: effect not implemented — do not guess mechanics.
Strong Energy (XY10 #115): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card can only be attached to Fighting Pokémon. This card provides Fighting Energy only while this card is attached to a Fighting Pokémon.
  - The attacks of the Fighting Pokémon this card is attached to do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - (If this card is attached to anything other than a Fighting Pokémon, discard this card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e102d84e-7447-5283-b2b4-db32af71a0c1",
    key="XY10",
    name="Strong Energy",
    display_name="Strong Energy",
    searchable_by=["Strong Energy", "Special"],
    subtypes=["Special"],
    collector_number=115,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
