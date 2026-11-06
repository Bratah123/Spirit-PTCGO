from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import oracle


card = SupporterCardDef(
    guid="3358863d-bf4d-575d-b784-04f0754a6116",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Oracle.Name",
    display_name="Oracle",
    searchable_by=["Oracle", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=oracle,
)
