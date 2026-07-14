from spirit.game.card_effects.trainers import professor_laventon, professor_laventon_playable
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c319540d-5b30-52f4-a742-5f2908567cc5",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorLaventon.Name",
    display_name="Professor Laventon",
    searchable_by=["Professor Laventon", "Supporter"],
    subtypes=["Supporter"],
    collector_number=162,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    effect=professor_laventon,
    condition=professor_laventon_playable
)
