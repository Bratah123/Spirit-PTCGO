from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="132ad4d9-8492-544c-afd9-f8899fd7ac12",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureModule.Name",
    display_name="Lure Module",
    searchable_by=["Lure Module", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="PGO",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
