from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


def _is_water_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.WATER.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


def archies_ace_condition(board, player_id):
    """You can play this card only when it is the last card in your hand."""
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) == 1


async def archies_ace(ctx):
    """Put a Water Pokemon from your discard pile onto your Bench. Then, draw 5 cards."""
    cards = [c for c in ctx.discard_pile() if _is_water_pokemon(c)]
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    if cards and bench is not None and len(bench.children) < effective_bench_capacity(ctx.board, ctx.player_id):
        picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Water Pokémon")
        if picks:
            await ctx.bench_pokemon(picks[0])
    await ctx.draw_cards(5)


card = SupporterCardDef(
    guid="e3b7848d-04cc-59df-a460-9f2d8f422c32",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArchiesAceintheHole.Name",
    display_name="Archie's Ace in the Hole",
    searchable_by=["Archie's Ace in the Hole", "Supporter"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    effect=archies_ace,
    condition=archies_ace_condition
)
