from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import crasher_wake, crasher_wake_condition

card = SupporterCardDef(
    guid="807f8cdd-a4a5-5433-b4e7-063c48cb3744",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrasherWake.Name",
    display_name="Crasher Wake",
    searchable_by=["Crasher Wake", "Supporter"],
    subtypes=["Supporter"],
    collector_number=129,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    condition=crasher_wake_condition,
    effect=crasher_wake,
)
