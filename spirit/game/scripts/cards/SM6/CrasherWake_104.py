from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import crasher_wake, crasher_wake_condition

card = SupporterCardDef(
    guid="33528646-2ab5-5dab-91c5-b0f7610b8d5c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrasherWake.Name",
    display_name="Crasher Wake",
    searchable_by=["Crasher Wake", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    condition=crasher_wake_condition,
    effect=crasher_wake,
)
