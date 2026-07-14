from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="654fda60-9a95-54fd-9f0d-a4df9c7d55a6",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
