from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class _ExcitingShake(Passive):
    """Marker: next turn, Prickly Needles flips 6 coins instead of 2."""


async def _exciting_shake(ctx):
    """During your next turn, flip 6 coins instead of 2 for Prickly Needles."""
    ctx.add_passive_through_own_next_turn(ctx.attacker, _ExcitingShake())


def _shaken(ctx):
    me = ctx.attacker
    turn = ctx.session.turn_state.turn_number
    return any(isinstance(t.passive, _ExcitingShake) and t.carrier_entity_id == me.entity_id
               and (t.expires_after_turn is None or t.expires_after_turn >= turn)
               for t in ctx.board.temporary_passives)


async def _prickly_needles(ctx):
    """Flip 2 coins (6 after Exciting Shake): 20 damage times the heads."""
    coins = 6 if _shaken(ctx) else 2
    results = await ctx.flip_coins(coins, ctx.ability.title) or []
    await ctx.deal_damage(20 * sum(1 for r in results if r))


card = PokemonCardDef(
    guid="b6328748-aa4a-51c6-aab5-9e51b2c31d3a",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic", "Maractus"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=556,
    abilities=[
        Attack(
            title="Exciting Shake",
            game_text="During your next turn, flip 6 coins instead of 2 for this Pok\u00e9mon's Prickly Needles attack.",
            cost={PokemonTypes.GRASS: 1},
            effect=_exciting_shake,
        ),
        Attack(
            title="Prickly Needles",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=_prickly_needles,
        ),
    ],
)