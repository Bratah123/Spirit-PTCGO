from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def tantailizing(ctx):
    """Flip a coin. If heads, switch 1 of your opponent's Benched Pokémon
    with their Active Pokémon."""
    heads = (await ctx.flip_coins(1, "Tantailizing"))[0]
    if not heads:
        return
    old_active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if old_active is None or not bench:
        return
    if ctx.effects_blocked(old_active):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon"
    ) or bench[0]
    await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="5810abb4-e330-53d0-9ee6-46ca0bdbd1a6",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    display_name="Fennekin",
    searchable_by=["Fennekin", "Basic", "Fennekin"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=653,
    abilities=[
        Attack(
            title="Invite Out",
            game_text="Flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tantailizing,
        ),
    ],
)