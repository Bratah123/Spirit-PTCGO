from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_basic_pokemon


async def egg_incubator(ctx):
    """Flip a coin. Heads: search a Basic Pokemon onto your Bench, shuffle.
    Tails: put this card on the bottom of your deck instead of the discard pile."""
    heads = (await ctx.flip_coins(1, "Egg Incubator"))[0]
    if heads:
        await search_to_bench(
            predicate=is_basic_pokemon, count=1,
            prompt="Choose a Basic Pokémon to put onto your Bench.",
        )(ctx)
    else:
        await ctx.put_on_bottom_of_deck(ctx.source)


card = ItemCardDef(
    guid="440d3bd9-bc70-5512-ba16-a634259fc77d",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EggIncubator.Name",
    display_name="Egg Incubator",
    searchable_by=["Egg Incubator", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="PGO",
    rarity=Rarities.RareSecret,
    effect=egg_incubator,
)
