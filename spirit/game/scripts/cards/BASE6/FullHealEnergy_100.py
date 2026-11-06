"""STUB: effect not implemented — do not guess mechanics.
Full Heal Energy (BASE6 #100): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - If you play this card from your hand, the Pokémon you attach it to is no longer affected by a Special Condition. Full Heal Energy provides Colorless energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5389cfad-55a2-5bce-813e-25debf5dd28a",
    key="BASE6",
    name="Full Heal Energy",
    display_name="Full Heal Energy",
    searchable_by=["Full Heal Energy", "Special"],
    subtypes=["Special"],
    collector_number=100,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
