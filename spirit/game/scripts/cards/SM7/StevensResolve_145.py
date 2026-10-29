from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    stevens_resolve,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="e274e0be-74d8-58c2-b796-9200f85d3341",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensResolve.Name",
    display_name="Steven's Resolve",
    searchable_by=["Steven's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    effect=stevens_resolve,
    condition=deck_nonempty,
)
