from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import trekking_shoes

card = ItemCardDef(
    guid="26078098-6684-50ff-89c5-815ba6957938",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrekkingShoes.Name",
    display_name="Trekking Shoes",
    searchable_by=["Trekking Shoes", "Item"],
    subtypes=["Item"],
    collector_number=215,
    set_code="SWSH10",
    rarity=Rarities.RareSecret,
    effect=trekking_shoes
)
