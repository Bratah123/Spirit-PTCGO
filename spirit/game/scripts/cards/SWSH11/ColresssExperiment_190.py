from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import colresss_experiment

card = SupporterCardDef(
    guid="b710e37a-6235-5155-a645-16ee63019f36",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColresssExperiment.Name",
    display_name="Colress's Experiment",
    searchable_by=["Colress's Experiment", "Supporter"],
    subtypes=["Supporter"],
    collector_number=190,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    effect=colresss_experiment,
)
