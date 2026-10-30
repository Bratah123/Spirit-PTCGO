"""STUB: effect not implemented — do not guess mechanics.
Energy Search (DP5 #90): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3afedf74-0a26-5162-9f9d-2bacb3ed80a1",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="DP5",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
