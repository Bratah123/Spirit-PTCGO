"""STUB: effect not implemented — do not guess mechanics.
Mystery Energy (XY4 #112): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card can only be attached to Psychic Pokémon. This card provides Psychic Energy only while this card is attached to a Psychic Pokémon.
  - The Retreat Cost of the Pokémon this card is attached to is ColorlessColorless less.
  - (If this card is attached to anything other than a Psychic Pokémon, discard this card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e85fead9-af5a-5f80-a84b-dede2d56e2d3",
    key="XY4",
    name="Mystery Energy",
    display_name="Mystery Energy",
    searchable_by=["Mystery Energy", "Special"],
    subtypes=["Special"],
    collector_number=112,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
