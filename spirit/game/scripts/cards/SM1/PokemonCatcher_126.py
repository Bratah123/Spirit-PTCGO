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
    guid="0226b7ac-a852-5ab7-8988-47f9bd363d27",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=126,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=pokemon_catcher,
    condition=opponent_has_bench
)
