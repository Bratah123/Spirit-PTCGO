from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7b1ba5c0-a429-58d1-87d7-b5d09a7548cd",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=132,
    set_code="BW7",
    rarity=Rarities.Common,
    effect=unimplemented
)
