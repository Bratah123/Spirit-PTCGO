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
    guid="02f84ed1-bd92-5d2c-ac8d-45ba09986d81",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="PokÃ©mon Catcher",
    searchable_by=["Pok\u00c3\u00a9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=pokemon_catcher,
    condition=opponent_has_bench
)
