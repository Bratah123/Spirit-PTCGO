from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="440d3bd9-bc70-5512-ba16-a634259fc77d",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EggIncubator.Name",
    display_name="Egg Incubator",
    searchable_by=["Egg Incubator", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="PGO",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
