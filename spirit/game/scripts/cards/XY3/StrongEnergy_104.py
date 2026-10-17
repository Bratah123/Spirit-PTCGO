"""STUB: effect not implemented — do not guess mechanics.
Strong Energy (XY3 #104): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card can only be attached to Fighting Pokémon. This card provides Fighting Energy only while this card is attached to a Fighting Pokémon.
  - The attacks of the Fighting Pokémon this card is attached to do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - (If this card is attached to anything other than a Fighting Pokémon, discard this card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="fc0679c9-79b4-5356-96e0-621c6296dabb",
    key="XY3",
    name="Strong Energy",
    display_name="Strong Energy",
    searchable_by=["Strong Energy", "Special"],
    subtypes=["Special"],
    collector_number=104,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
