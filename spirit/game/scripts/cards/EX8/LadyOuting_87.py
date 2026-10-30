from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import lady_outing
from spirit.game.card_effects.trainers import deck_nonempty


card = SupporterCardDef(
    guid="36d1a2b0-3ffe-5c76-8c00-213f72554996",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LadyOuting.Name",
    display_name="Lady Outing",
    searchable_by=["Lady Outing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    effect=lady_outing,
    condition=deck_nonempty,
)
