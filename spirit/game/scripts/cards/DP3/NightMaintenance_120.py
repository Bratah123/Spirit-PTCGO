"""Night Maintenance (DP2 #113)."""
from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.card_effects.dp import night_maintenance

card = ItemCardDef(
    guid="165c29f7-1263-5c87-a6d0-d3e2f40da45d",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightMaintenance.Name",
    display_name="Night Maintenance",
    searchable_by=["Night Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=night_maintenance(),
)
