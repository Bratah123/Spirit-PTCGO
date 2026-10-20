from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import requires_hand


async def pokemon_communication(ctx):
    """Reveal a Pokemon in your hand and put it on top of your deck. If you do,
    search your deck for a Pokemon, reveal it, and put it into your hand.
    Shuffle your deck afterward."""
    candidates = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose a Pokémon to put on top of your deck.",
    )
    if not picks:
        return
    await ctx.reveal_cards(picks)
    await ctx.put_on_top_of_deck(picks[0])
    found = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=0,
        prompt="Choose a Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="a56be50f-cbcd-52d4-bf26-809a91cafd03",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pokémon Communication", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    condition=requires_hand(is_pokemon_card, n=1),
    effect=pokemon_communication,
)
