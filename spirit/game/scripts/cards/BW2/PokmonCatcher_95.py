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
    guid="0a553e6a-00d3-5d43-b06f-bd4871199325",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pok\u00e9mon Catcher",
    searchable_by=["Pokémon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=pokemon_catcher,
    condition=opponent_has_bench
)
