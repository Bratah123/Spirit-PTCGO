from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    stevens_resolve,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="4fd6fca6-1def-5d7a-9eb1-45de50325b0b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensResolve.Name",
    display_name="Steven's Resolve",
    searchable_by=["Steven's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=stevens_resolve,
    condition=deck_nonempty,
)
