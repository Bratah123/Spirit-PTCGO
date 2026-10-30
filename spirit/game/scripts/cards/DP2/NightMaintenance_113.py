"""Night Maintenance (DP2 #113)."""
from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.card_effects.dp import night_maintenance

card = ItemCardDef(
    guid="352ceac9-0ecf-52dc-9703-0cb90904fa01",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightMaintenance.Name",
    display_name="Night Maintenance",
    searchable_by=["Night Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=113,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=night_maintenance(),
)
