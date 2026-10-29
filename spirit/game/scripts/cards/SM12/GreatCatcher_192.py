from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import great_catcher, great_catcher_condition

card = ItemCardDef(
    guid="790a9393-4d88-50ef-9dbe-0ce83805d7bd",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatCatcher.Name",
    display_name="Great Catcher",
    searchable_by=["Great Catcher", "Item"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=great_catcher, condition=great_catcher_condition,
)
