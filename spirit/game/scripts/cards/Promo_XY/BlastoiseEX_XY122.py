from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches


async def _rapid_spin(ctx):
    """Printed damage; switch this Pokemon with 1 of your Benched Pokemon,
    then your opponent switches their Active with 1 of their Benched."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        await ctx.switch_active(ctx.player_id, target or bench[0])
        await ctx.flush_choreography()
    await opponent_switches(ctx)


async def _splash_bomb_heads(ctx):
    """120; flip a coin. If heads, this Pokemon does 30 damage to itself
    (as printed on this promo)."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="4ca96bbb-b936-520f-972a-efe18f7ef593",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name",
    display_name="Blastoise-EX",
    searchable_by=["Blastoise-EX", "Basic", "EX", "BlastoiseEX"],
    subtypes=["Basic", "EX"],
    collector_number=122,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=9,
    abilities=[
        Attack(
            title="Rapid Spin",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. The, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_rapid_spin,
        ),
        Attack(
            title="Splash Bomb",
            game_text="Flip a coin. If heads, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=_splash_bomb_heads,
        ),
    ],
)