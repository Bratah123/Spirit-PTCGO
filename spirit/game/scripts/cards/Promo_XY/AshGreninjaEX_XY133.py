from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _dancing_shuriken(ctx):
    """Flip 3 coins: 20 times heads to 1 of the opponent's Pokemon (no W/R on the Bench)."""
    results = await ctx.flip_coins(3, ctx.ability.title)
    heads = sum(1 for r in results if r)
    pool = ctx.opponent_pokemon_in_play()
    if not heads or not pool:
        return
    target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, f"Choose a Pokémon to take {20 * heads} damage")
    if target is not None:
        await ctx.deal_damage(20 * heads, target=target)


card = PokemonCardDef(
    guid="8d76a55a-dd34-5d5a-9b85-f6860b1a9bbf",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AshGreninjaEX.Name",
    display_name="Ash-Greninja-EX",
    searchable_by=["Ash-Greninja-EX", "Basic", "EX", "AshGreninjaEX"],
    subtypes=["Basic", "EX"],
    collector_number=133,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=658,
    abilities=[
        Attack(
            title="Dancing Shuriken",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=_dancing_shuriken,
        ),
        Attack(
            title="Ninja Blade",
            game_text="This Pok\u00e9mon can't use Ninja Blade during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)