from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import red_blue, red_blue_condition

card = SupporterCardDef(
    guid="42a54f77-ffd1-51ac-8175-70de265f2b2c",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedBlue.Name",
    display_name="Red & Blue",
    searchable_by=["Red & Blue", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=234,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=red_blue, condition=red_blue_condition,
)
