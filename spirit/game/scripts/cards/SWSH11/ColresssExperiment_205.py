from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import colresss_experiment

card = SupporterCardDef(
    guid="e9933893-f67c-5952-ba97-58c973305aa9",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColresssExperiment.Name",
    display_name="Colress's Experiment",
    searchable_by=["Colress's Experiment", "Supporter"],
    subtypes=["Supporter"],
    collector_number=205,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    effect=colresss_experiment,
)
