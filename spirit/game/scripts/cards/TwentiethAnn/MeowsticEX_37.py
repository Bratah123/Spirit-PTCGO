from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import _is_damaged


async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)


def _shadow_ear_condition(board, player_id, pokemon=None):
    return pokemon is not None and board.active_pokemon(player_id) is pokemon and any(
        _is_damaged(board, p) for p in board.pokemon_in_play(player_id))


async def _shadow_ear(ctx):
    """If this Pokemon is your Active: move 1 damage counter from 1 of your
    Pokemon to 1 of your opponent's Pokemon."""
    pool = [p for p in ctx.my_pokemon_in_play() if _is_damaged(ctx.board, p)]
    if not pool:
        return
    src = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Move a damage counter from which Pokémon?")
    if src is not None:
        await ctx.move_damage_counters(src, ctx.opponent_pokemon_in_play(), max_count=1)


card = PokemonCardDef(
    guid="74e60f4b-6ca9-5826-85e6-f254bdd5368a",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeowsticEX.Name",
    display_name="Meowstic-EX",
    searchable_by=["Meowstic-EX", "Basic", "EX", "MeowsticEX"],
    subtypes=["Basic", "EX"],
    collector_number=37,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=678,
    abilities=[
        Ability(
            title="Shadow Ear",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may move 1 damage counter from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_shadow_ear_condition,
            effect=_shadow_ear,
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=sonic_boom,
        ),
    ],
)