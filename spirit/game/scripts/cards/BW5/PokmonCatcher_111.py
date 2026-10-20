from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_bench


async def pokemon_catcher(ctx):
    """Switch 1 of your opponent's Benched Pok\u00e9mon with their Active (no flip in this print)."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your opponent's new Active Pok\u00e9mon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = ItemCardDef(
    guid="53921195-6aad-521d-ad1d-645be1d0cc67",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=111,
    set_code="BW5",
    rarity=Rarities.RareSecret,
    effect=pokemon_catcher,
    condition=opponent_has_bench
)
