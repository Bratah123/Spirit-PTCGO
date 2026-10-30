from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import wallys_training
from spirit.game.card_effects.trainers import deck_nonempty


card = SupporterCardDef(
    guid="94b26df7-2743-56d6-9c36-aa4d7d250257",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WallysTraining.Name",
    display_name="Wally's Training",
    searchable_by=["Wally's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    effect=wallys_training,
    condition=deck_nonempty,
)
