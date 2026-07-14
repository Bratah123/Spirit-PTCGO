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
    guid="d4644be3-57c5-546d-aeec-4cb076dd48ed",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="PokÃ© Ball",
    searchable_by=["PokÃ© Ball", "Item"],
    subtypes=["Item"],
    collector_number=137,
    set_code="CZ",
    rarity=Rarities.Common,
    effect=poke_ball
)
