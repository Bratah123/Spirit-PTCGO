"""STUB: effect not implemented — do not guess mechanics.
Burning Energy (XY8 #151): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card can only be attached to Fire Pokémon. This card provides Fire Energy only while this card is attached to a Fire Pokémon.
  - If this card is discarded by an attack of the Fire Pokémon this card is attached to, attach this card from your discard pile to that Pokémon after attacking.
  - (If this card is attached to anything other than a Fire Pokémon, discard this card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="b7240297-72ff-53ce-be7b-66c217daca3f",
    key="XY8",
    name="Burning Energy",
    display_name="Burning Energy",
    searchable_by=["Burning Energy", "Special"],
    subtypes=["Special"],
    collector_number=151,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
