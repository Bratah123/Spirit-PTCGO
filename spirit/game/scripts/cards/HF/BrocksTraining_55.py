from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.hf import brocks_training, brocks_training_condition

card = SupporterCardDef(
    guid="c9f5e4ac-36a4-5da9-acf1-d84198fbd72e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksTraining.Name",
    display_name="Brock's Training",
    searchable_by=["Brock's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=55,
    set_code="HF",
    rarity=Rarities.RareHolo,
    effect=brocks_training,
    condition=brocks_training_condition,
)
