from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import wallys_training
from spirit.game.card_effects.trainers import deck_nonempty


card = SupporterCardDef(
    guid="1ee6d896-ba61-59ee-b459-d49a8a49f6cc",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WallysTraining.Name",
    display_name="Wally's Training",
    searchable_by=["Wally's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=wallys_training,
    condition=deck_nonempty,
)
