from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_special_energy


def _pool(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return [c for c in (discard.children if discard else []) if is_special_energy(c)]


def special_charge_condition(board, player_id):
    return bool(_pool(board, player_id))


async def special_charge(ctx):
    """Shuffle 2 Special Energy cards from your discard pile into your deck."""
    pool = _pool(ctx.board, ctx.player_id)
    n = min(2, len(pool))
    picked = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose Special Energy cards")
    if picked:
        await ctx.shuffle_into_deck(picked)


card = ItemCardDef(
    guid="ee453dd2-a4f6-5919-b5bd-83cf7435124b",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpecialCharge.Name",
    display_name="Special Charge",
    searchable_by=["Special Charge", "Item"],
    subtypes=["Item"],
    collector_number=105,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    condition=special_charge_condition,
    effect=special_charge
)
