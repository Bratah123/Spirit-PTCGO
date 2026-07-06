from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6f38eb37-416a-53b6-b0c9-948c201994d0",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
