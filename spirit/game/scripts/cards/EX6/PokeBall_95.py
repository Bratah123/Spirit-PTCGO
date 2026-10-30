from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card

_search = search_to_hand(
    is_pokemon_card, count=1, minimum=0, reveal=True,
    prompt="Choose a Basic Pokémon or Evolution card to put into your hand.",
)


async def poke_ball(ctx):
    """Flip a coin. If heads, search the deck for a Basic Pokémon or Evolution
    card, reveal it, and put it into your hand. Then shuffle."""
    results = await ctx.flip_coins(1, "Poké Ball")
    if results and results[0]:
        await _search(ctx)


card = ItemCardDef(
    guid="988492e4-da67-59b0-9594-0d34e5734d38",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=poke_ball,
)
