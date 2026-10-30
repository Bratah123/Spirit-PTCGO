"""Buck's Training (DP6 #130)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import bucks_training

card = SupporterCardDef(
    guid="fa368c4f-f5f1-568a-abd6-199c9a693d29",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BucksTraining.Name",
    display_name="Buck's Training",
    searchable_by=["Buck's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    effect=bucks_training(),
)
