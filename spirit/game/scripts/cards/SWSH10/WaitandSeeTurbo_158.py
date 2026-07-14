from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


def _wait_and_see_turbo_condition(board, player_id):
    """Only usable if you go second, during your first turn (turn 2)."""
    turn_state = getattr(board, "turn_state", None)
    return turn_state is not None and turn_state.turn_number == 2


async def wait_and_see_turbo(ctx):
    """Search your deck for a basic Energy card and attach it to 1 of your
    Pokemon. Shuffle your deck. Your turn ends."""
    await search_attach_energy(predicate=is_basic_energy_card, count=1)(ctx)
    ctx.ends_turn = True


card = ItemCardDef(
    guid="75fe9eb1-0726-5b62-8930-852a8812098a",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaitandSeeTurbo.Name",
    display_name="Wait and See Turbo",
    searchable_by=["Wait and See Turbo", "Item"],
    subtypes=["Item"],
    collector_number=158,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    condition=_wait_and_see_turbo_condition,
    effect=wait_and_see_turbo,
)
