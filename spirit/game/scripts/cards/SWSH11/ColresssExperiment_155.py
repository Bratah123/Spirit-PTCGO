from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import colresss_experiment, deck_nonempty

card = SupporterCardDef(
    guid="67b4bcb1-f01b-540e-bf35-aa3f326f08ba",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColresssExperiment.Name",
    display_name="Colress's Experiment",
    searchable_by=["Colress's Experiment", "Supporter"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=colresss_experiment,
)
