from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import good_manners, good_manners_condition


card = ItemCardDef(
    guid="ebb39525-5bf3-5a07-a618-0b40b165e1ad",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoodManners.Name",
    display_name="Good Manners",
    searchable_by=["Good Manners"],
    subtypes=[],
    collector_number=111,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    condition=good_manners_condition,
    effect=good_manners,
)
