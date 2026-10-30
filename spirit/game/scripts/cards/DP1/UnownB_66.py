"""STUB: effect not implemented — do not guess mechanics.
Unown [B] (DP1 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import unown_bounce, unown_bench_condition, poke_power_condition
from spirit.game.data_utils import Activations

card = PokemonCardDef(
    guid="0137eec0-9774-5387-bb35-07daf5a4f35f",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownB.Name",
    display_name="Unown [B]",
    searchable_by=["Unown [B]", "Basic", "UnownB"],
    subtypes=["Basic"],
    collector_number=66,
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
            title="BOUNCE",
            game_text="Once during your turn (before your attack), if Unown B is on your Bench, you may flip a coin. If heads, discard all cards attached to any 1 of your Unown and shuffle that Pok\u00e9mon back into your deck.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=poke_power_condition(unown_bench_condition),
            activation=Activations.ONCE_PER_TURN,
            effect=unown_bounce(),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)