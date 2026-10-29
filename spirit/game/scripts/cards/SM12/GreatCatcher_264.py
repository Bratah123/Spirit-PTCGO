from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import great_catcher, great_catcher_condition

card = ItemCardDef(
    guid="34b89b48-244f-5cdf-8036-f1c642f7797d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatCatcher.Name",
    display_name="Great Catcher",
    searchable_by=["Great Catcher", "Item"],
    subtypes=["Item"],
    collector_number=264,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    effect=great_catcher, condition=great_catcher_condition,
)
