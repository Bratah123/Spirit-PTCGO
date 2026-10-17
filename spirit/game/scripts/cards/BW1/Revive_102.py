from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cd12e318-73dd-53d2-ad1f-0b39c092ff6a",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
