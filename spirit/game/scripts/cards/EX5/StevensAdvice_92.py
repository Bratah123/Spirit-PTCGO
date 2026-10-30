from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import stevens_advice, stevens_advice_condition

card = SupporterCardDef(
    guid="25e2b4fb-8b58-5b04-a194-09894b6545c3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensAdvice.Name",
    display_name="Steven's Advice",
    searchable_by=["Steven's Advice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    condition=stevens_advice_condition,
    effect=stevens_advice,
)
