from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5f72f28f-27d0-56b3-9cfb-1e9b39fbd7fe",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=112,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
