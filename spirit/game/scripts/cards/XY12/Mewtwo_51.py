from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.passives_common import protect_next_turn


_BARRIER_USED = {}


def _barrier_condition(board, player_id, pokemon=None):
    """Not usable if 1 of your Pokemon used Barrier during your last turn."""
    ts = getattr(board, "turn_state", None)
    return ts is None or _BARRIER_USED.get(player_id) != ts.turn_number - 2


async def _barrier(ctx):
    """During the opponent's next turn, prevent all effects of attacks,
    including damage, done to this Pokemon."""
    _BARRIER_USED[ctx.player_id] = ctx.session.turn_state.turn_number
    await protect_next_turn(prevent=True, effects_too=True)(ctx)


card = PokemonCardDef(
    guid="5308c025-6003-5773-84be-8886e9b419dc",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 20, base=20),
        ),
        Attack(
            title="Barrier",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to this Pok\u00e9mon. If 1 of your Pok\u00e9mon used Barrier during your last turn, this attack can't be used.",
            cost={PokemonTypes.PSYCHIC: 2},
            condition=_barrier_condition,
            effect=_barrier,
        ),
    ],
)