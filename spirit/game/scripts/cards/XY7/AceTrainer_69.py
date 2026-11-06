from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw


def ace_trainer_condition(board, player_id):
    """Only if you have more Prize cards left than your opponent."""
    mine = board.find_player_area(player_id, "prizePile")
    opp_id = next((pid for pid in board.player_ids if pid != player_id), None)
    theirs = board.find_player_area(opp_id, "prizePile") if opp_id else None
    return mine is not None and theirs is not None and len(mine.children) > len(theirs.children)


card = SupporterCardDef(
    guid="a1cdecf5-5c0e-5f3c-bf0f-16e31db744d8",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AceTrainer.Name",
    display_name="Ace Trainer",
    searchable_by=["Ace Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_into_deck_draw(6, opponent_n=3),
    condition=ace_trainer_condition
)
