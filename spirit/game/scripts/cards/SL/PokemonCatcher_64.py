from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_bench


async def pokemon_catcher(ctx):
    """Switch 1 of your opponent's Benched Pokémon with their Active Pokémon."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose your opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = ItemCardDef(
    guid="ff13f3cf-5e8c-58d0-baf5-683ab296b524",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=64,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=pokemon_catcher,
    condition=opponent_has_bench
)
