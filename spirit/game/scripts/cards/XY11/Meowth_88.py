from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _stall_condition(board, player_id, pokemon=None):
    """Only if you go second, and only on your first turn (turn 2)."""
    ts = getattr(board, "turn_state", None)
    return ts is not None and ts.turn_number == 2


async def _stall(ctx):
    """Discard an Energy attached to 1 of your opponent's Pokemon."""
    pool = [p for p in ctx.opponent_pokemon_in_play() if ctx.attached_energies(p) and not ctx.effects_blocked(p)]
    if not pool:
        return
    t = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Discard an Energy from which Pokémon?")
    if t is not None:
        await ctx.discard_energy_from(t, 1, minimum=1)


card = PokemonCardDef(
    guid="3ea441c9-e5a0-5a41-9464-3ced3fec063d",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Stall",
            game_text="You can use this attack only if you go second, and only on your first turn. Discard an Energy attached to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=_stall_condition,
            effect=_stall,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)