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
    guid="9691db53-6f93-52fa-9b3b-32a2a0701284",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=poke_ball,
)
