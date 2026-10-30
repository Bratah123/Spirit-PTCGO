"""STUB: effect not implemented — do not guess mechanics.
Unown [D] (DP1 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import unown_draw, unown_bench_condition, poke_power_condition
from spirit.game.data_utils import Activations

card = PokemonCardDef(
    guid="e7d0b874-c1c5-515a-bfac-69853efb6af9",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownD.Name",
    display_name="Unown [D]",
    searchable_by=["Unown [D]", "Basic", "UnownD"],
    subtypes=["Basic"],
    collector_number=68,
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
            title="DRAW",
            game_text="Once during your turn (before your attack), if Unown D is on your Bench, you may flip a coin. If heads, each player may draw a card. (You draw your card first.)",
            ability_type=AbilityTypes.POKE_POWER,
            condition=poke_power_condition(unown_bench_condition),
            activation=Activations.ONCE_PER_TURN,
            effect=unown_draw(),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)