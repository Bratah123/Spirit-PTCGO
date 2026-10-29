from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    tv_reporter,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="1c654575-c481-5dce-aabf-0f3142da2fc0",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=tv_reporter,
    condition=deck_nonempty,
)
