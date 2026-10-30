from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import stevens_advice, stevens_advice_condition

card = SupporterCardDef(
    guid="74016157-7106-526d-aaef-a70b0f76b93d",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensAdvice.Name",
    display_name="Steven's Advice",
    searchable_by=["Steven's Advice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    condition=stevens_advice_condition,
    effect=stevens_advice,
)
