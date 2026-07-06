from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0145e34c-d02b-5668-b779-814767f610f4",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WelcomingLantern.Name",
    display_name="Welcoming Lantern",
    searchable_by=["Welcoming Lantern", "Item", "Single Strike"],
    subtypes=["Item", "Single Strike"],
    collector_number=156,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
