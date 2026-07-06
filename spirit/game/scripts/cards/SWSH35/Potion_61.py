from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="71dc4fb3-ce42-51a8-940d-1684a0cfc130",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=61,
    set_code="SWSH35",
    rarity=Rarities.Common,
    effect=unimplemented
)
