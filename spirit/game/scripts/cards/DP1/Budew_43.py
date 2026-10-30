"""STUB: effect not implemented — do not guess mechanics.
Budew (DP1 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_trainer_card
from spirit.game.card_effects.dp import baby_evolution, baby_evolution_condition


card = PokemonCardDef(
    guid="ca33f874-78ac-5b02-a603-30e4c933b783",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Budew.Name",
    display_name="Budew",
    searchable_by=["Budew", "Basic", "Budew"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=406,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Roselia from your hand onto Budew (this counts as evolving Budew) and remove all damage counters from Budew.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=baby_evolution_condition('Roselia'),
            effect=baby_evolution('Roselia'),
        ),
        Attack(
            title="Errand-Running",
            game_text="Search your deck for a Trainer card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=search_to_hand(is_trainer_card, count=1, reveal=True, prompt='Choose a Trainer card.'),
        ),
    ],
)