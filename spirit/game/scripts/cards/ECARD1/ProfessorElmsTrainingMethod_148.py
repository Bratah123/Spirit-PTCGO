from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_evolution_pokemon


card = SupporterCardDef(
    guid="36532a6a-fb17-52bb-921d-8960bc799bae",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_evolution_pokemon, count=1, minimum=0, reveal=True,
        prompt="Choose an Evolution card to put into your hand.",
    ),
)
