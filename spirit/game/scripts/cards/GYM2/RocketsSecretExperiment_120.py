from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import rockets_secret_experiment


card = ItemCardDef(
    guid="1ae6d970-ac31-55fd-b0e0-24e7cfbd7f74",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSecretExperiment.Name",
    display_name="Rocket's Secret Experiment",
    searchable_by=["Rocket's Secret Experiment"],
    subtypes=[],
    collector_number=120,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    effect=rockets_secret_experiment,
)
