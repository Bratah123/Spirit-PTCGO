from spirit.game.data_utils import StadiumCardDef, Ability, Activations, subtypes_for
from spirit.game.attributes import Rarities


def _is_single_strike_card(card):
    return "Single Strike" in subtypes_for(card.archetype_id)


def tower_of_darkness_condition(board, player_id, stadium):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_single_strike_card(c) for c in hand.children)


async def tower_of_darkness_ability(ctx):
    """Once during each player's turn, that player may draw 2 cards by
    discarding a Single Strike card from their hand."""
    picks = await ctx.choose_cards(
        [c for c in ctx.hand() if _is_single_strike_card(c)], 1, minimum=1,
        prompt="Discard a Single Strike card to draw 2 cards.",
    )
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.draw_cards(2)


card = StadiumCardDef(
    guid="97e3003b-223c-5631-88d6-1bdae2588e4e",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TowerofDarkness.Name",
    display_name="Tower of Darkness",
    searchable_by=["Tower of Darkness", "Stadium", "Single Strike"],
    subtypes=["Stadium", "Single Strike"],
    collector_number=137,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Tower of Darkness",
        game_text="Once during each player's turn, that player may draw 2 cards. In order to use this effect, that player must discard a Single Strike card from their hand.",
        activation=Activations.ONCE_PER_TURN,
        effect=tower_of_darkness_ability,
        condition=tower_of_darkness_condition,
    ),
)
