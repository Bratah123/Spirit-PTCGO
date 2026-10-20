from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.trainers import is_basic_energy_card


def _pool(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return [c for c in (discard.children if discard else [])
            if is_pokemon_card(c) or is_basic_energy_card(c)]


def brocks_grit_condition(board, player_id):
    return bool(_pool(board, player_id))


async def brocks_grit(ctx):
    """Shuffle 6 in any combination of Pokemon and basic Energy cards from your
    discard pile into your deck."""
    pool = _pool(ctx.board, ctx.player_id)
    n = min(6, len(pool))
    picked = pool if len(pool) == n else await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 6 cards to shuffle into your deck")
    if picked:
        await ctx.shuffle_into_deck(picked)


card = SupporterCardDef(
    guid="3c8374e7-c535-5236-af32-4ee397c08174",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY12",
    rarity=Rarities.RareUltra,
    condition=brocks_grit_condition,
    effect=brocks_grit
)
