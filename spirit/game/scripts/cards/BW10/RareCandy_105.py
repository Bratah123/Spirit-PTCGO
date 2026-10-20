from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6a7bcfd6-023a-59bf-9932-9053b3d78b08",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=105,
    set_code="BW10",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
