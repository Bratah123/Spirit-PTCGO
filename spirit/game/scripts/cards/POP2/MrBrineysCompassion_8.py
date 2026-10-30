from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import scoop_own_non_ex

card = SupporterCardDef(
    guid="19d6bada-d5a6-5c40-b604-f2b4854f0674",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrBrineysCompassion.Name",
    display_name="Mr. Briney's Compassion",
    searchable_by=["Mr. Briney's Compassion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=8,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    effect=scoop_own_non_ex(),
)
