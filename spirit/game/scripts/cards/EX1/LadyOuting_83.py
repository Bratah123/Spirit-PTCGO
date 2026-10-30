from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import lady_outing
from spirit.game.card_effects.trainers import deck_nonempty


card = SupporterCardDef(
    guid="ac7f1d27-12a0-5915-9d35-381764d4a119",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LadyOuting.Name",
    display_name="Lady Outing",
    searchable_by=["Lady Outing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=lady_outing,
    condition=deck_nonempty,
)
