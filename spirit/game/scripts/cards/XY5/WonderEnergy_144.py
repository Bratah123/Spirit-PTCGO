"""STUB: effect not implemented — do not guess mechanics.
Wonder Energy (XY5 #144): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card can only be attached to Fairy Pokémon. This card provides Fairy Energy only while this card is attached to a Fairy Pokémon.
  - Prevent all effects of your opponent's attacks, except damage, done to the Fairy Pokémon that this card is attached to. (Existing effects are not removed.)
  - (If this card is attached to anything other than a Fairy Pokémon, discard this card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8c8945f3-43a7-560c-9c0a-80cabe04ad53",
    key="XY5",
    name="Wonder Energy",
    display_name="Wonder Energy",
    searchable_by=["Wonder Energy", "Special"],
    subtypes=["Special"],
    collector_number=144,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
