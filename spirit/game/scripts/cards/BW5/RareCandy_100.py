from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4ee0212e-9995-5ac9-9e28-d8182150eb5a",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
