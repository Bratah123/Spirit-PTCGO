from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0e2e453f-ac42-5da4-be1c-26ecea0a0b34",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WelcomingLantern.Name",
    display_name="Welcoming Lantern",
    searchable_by=["Welcoming Lantern", "Item", "Single Strike"],
    subtypes=["Item", "Single Strike"],
    collector_number=230,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
