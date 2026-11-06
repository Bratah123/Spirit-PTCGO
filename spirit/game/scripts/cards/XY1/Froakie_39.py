from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _bounce(ctx):
    """10; flip a coin. If heads, switch this Pokemon with 1 of your Benched."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    bench = ctx.my_bench()
    if results and results[0] and bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        await ctx.switch_active(ctx.player_id, target or bench[0])


card = PokemonCardDef(
    guid="94c16d26-e9b4-5f51-8f77-252d2a85af41",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    display_name="Froakie",
    searchable_by=["Froakie", "Basic", "Froakie"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=656,
    abilities=[
        Attack(
            title="Bounce",
            game_text="Flip a coin. If heads, switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=_bounce,
        ),
    ],
)