from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities


def _rose_tower_condition(board, player_id, stadium):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len(hand.children) < 3


async def _rose_tower_effect(ctx):
    if await ctx.ask_yes_no("Draw cards until you have 3 cards in your hand?"):
        await ctx.draw_until(3)


ROSE_TOWER_ABILITY = Ability(
    title="Rose Tower",
    game_text="Once during each player's turn, that player may draw cards until they have 3 cards in their hand.",
    activation=Activations.ONCE_PER_TURN,
    condition=_rose_tower_condition,
    effect=_rose_tower_effect,
)

card = StadiumCardDef(
    guid="2c6fa6b9-5fc8-5870-b10a-95cd47339c50",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoseTower.Name",
    display_name="Rose Tower",
    searchable_by=["Rose Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=169,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    ability=ROSE_TOWER_ABILITY,
)
