from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="10bee995-3c57-5f12-98d3-3f1b45c62180",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EggIncubator.Name",
    display_name="Egg Incubator",
    searchable_by=["Egg Incubator", "Item"],
    subtypes=["Item"],
    collector_number=66,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
