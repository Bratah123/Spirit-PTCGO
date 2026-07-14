from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_bench


async def pokemon_catcher(ctx):
    """Flip a coin. If heads, switch 1 of the opponent's Benched Pokemon
    with their Active Pokemon."""
    if not (await ctx.flip_coins(1, "Pokémon Catcher"))[0]:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose your opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = ItemCardDef(
    guid="14cbcefb-fac6-56ca-8a73-9d93e81c7699",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="PokÃ©mon Catcher",
    searchable_by=["PokÃ©mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=pokemon_catcher,
    condition=opponent_has_bench
)
