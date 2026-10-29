from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import red_blue, red_blue_condition

card = SupporterCardDef(
    guid="cb8c5531-c0bb-5f15-b2e5-0095e1fcb873",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedBlue.Name",
    display_name="Red & Blue",
    searchable_by=["Red & Blue", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=202,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=red_blue, condition=red_blue_condition,
)
