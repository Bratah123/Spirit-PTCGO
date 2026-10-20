from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


def _is_fighting_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.FIGHTING.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


def maxies_trick_condition(board, player_id):
    """You can play this card only when it is the last card in your hand."""
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) == 1


async def maxies_trick(ctx):
    """Put a Fighting Pokemon from your discard pile onto your Bench. Then, draw 5 cards."""
    cards = [c for c in ctx.discard_pile() if _is_fighting_pokemon(c)]
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    if cards and bench is not None and len(bench.children) < effective_bench_capacity(ctx.board, ctx.player_id):
        picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Fighting Pokémon")
        if picks:
            await ctx.bench_pokemon(picks[0])
    await ctx.draw_cards(5)


card = SupporterCardDef(
    guid="efa04d27-1a71-5a98-a0d9-d7a99c2c6795",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxiesHiddenBallTrick.Name",
    display_name="Maxie's Hidden Ball Trick",
    searchable_by=["Maxie's Hidden Ball Trick", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=maxies_trick,
    condition=maxies_trick_condition
)
