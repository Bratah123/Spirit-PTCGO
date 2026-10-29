from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    tv_reporter,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="9e8e4f82-9912-5d22-8c89-2bdec7a1f04f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=tv_reporter,
    condition=deck_nonempty,
)
