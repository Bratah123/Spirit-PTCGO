"""STUB: effect not implemented — do not guess mechanics.
Beginning Door (DPP #DP54): trainer effect stubbed.

Card text:
  - Search your deck for Arceus, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="975b44be-db60-524a-bfcd-ffcb09eb1e61",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeginningDoor.Name",
    display_name="Beginning Door",
    searchable_by=["Beginning Door", "Item"],
    subtypes=["Item"],
    collector_number=54,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
