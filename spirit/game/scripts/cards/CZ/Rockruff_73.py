from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def invite_out(ctx):
    """Flip a coin. If heads, switch 1 of your opponent's Benched Pokémon
    with their Active Pokémon."""
    heads = (await ctx.flip_coins(1, "Invite Out"))[0]
    if not heads:
        return
    active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if active is None or not bench or ctx.effects_blocked(active):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon"
    ) or bench[0]
    await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="498a4795-0542-573f-96e5-54f951ec5e36",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    display_name="Rockruff",
    searchable_by=["Rockruff", "Basic", "Rockruff"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="CZ",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=744,
    abilities=[
        Attack(
            title="Invite Out",
            game_text="Flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=invite_out,
        ),
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)