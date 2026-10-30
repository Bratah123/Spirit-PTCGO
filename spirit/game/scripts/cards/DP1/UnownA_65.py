"""STUB: effect not implemented — do not guess mechanics.
Unown [A] (DP1 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import unown_analyze, unown_bench_condition, poke_power_condition
from spirit.game.data_utils import Activations

card = PokemonCardDef(
    guid="3954315f-07a1-537a-b314-828b5e65d250",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownA.Name",
    display_name="Unown [A]",
    searchable_by=["Unown [A]", "Basic", "UnownA"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="ANALYZE",
            game_text="Once during your turn (before your attack), if Unown A is on your Bench, you may look at the top 2 cards of your deck and put them back on top of your deck in any order.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=poke_power_condition(unown_bench_condition),
            activation=Activations.ONCE_PER_TURN,
            effect=unown_analyze(),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)