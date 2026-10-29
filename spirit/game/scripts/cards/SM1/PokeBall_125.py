from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


async def poke_ball(ctx):
    """Flip a coin. If heads, search the deck for a Pokemon, reveal it, and
    put it into your hand. Then, shuffle your deck."""
    if (await ctx.flip_coins(1, "Poké Ball"))[0]:
        picks = await ctx.search_deck(
            is_pokemon_card, count=1, minimum=0,
            prompt="Choose a Pokémon to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()


card = ItemCardDef(
    guid="35d23b4c-20d2-55a6-8cdf-7313cd0f60af",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=poke_ball,
)
