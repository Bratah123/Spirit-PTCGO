from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import scoop_own_non_ex

card = SupporterCardDef(
    guid="5b5fbb62-9deb-5d0f-b292-ea82dbc5d051",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrBrineysCompassion.Name",
    display_name="Mr. Briney's Compassion",
    searchable_by=["Mr. Briney's Compassion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    effect=scoop_own_non_ex(),
)
