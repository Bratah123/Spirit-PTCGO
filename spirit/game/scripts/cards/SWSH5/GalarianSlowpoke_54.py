from spirit.game.data_utils import PokemonCardDef, Attack, Ability
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
    guid="843f8913-976d-512d-8b32-46b3eafe9068",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    display_name="Galarian Slowpoke",
    searchable_by=["Galarian Slowpoke", "Basic", "GalarianSlowpoke"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=79,
    abilities=[
        Attack(
            title="Tantailizing",
            game_text="Flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tantailizing,
        ),
    ],
)