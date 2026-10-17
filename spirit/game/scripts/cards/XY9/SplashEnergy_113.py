"""STUB: effect not implemented — do not guess mechanics.
Splash Energy (XY9 #113): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card can only be attached to Water Pokémon. This card provides Water Energy only while this card is attached to a Water Pokémon.
  - If the Water Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put that Pokémon into your hand. (Discard all cards attached to it.)
  - (If this card is attached to anything other than a Water Pokémon, discard this card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c7a9536c-e7b4-5e84-803b-f96379054d56",
    key="XY9",
    name="Splash Energy",
    display_name="Splash Energy",
    searchable_by=["Splash Energy", "Special"],
    subtypes=["Special"],
    collector_number=113,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
