"""Beginning Door (DPP #DP54)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import beginning_door

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
    effect=beginning_door(),
)
