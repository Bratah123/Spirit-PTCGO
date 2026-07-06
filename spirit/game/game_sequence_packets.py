from typing import Any, Dict, List, Optional
from spirit.game.attributes import GameSequence
from spirit.network.message_names import OutboundMsg

def _build_msg(name: str, value: Dict[str, Any]) -> Dict[str, Any]:
    """Helper to build standard Warg Protocol polymorphic JSON envelopes."""
    return {
        "name": name,
        "value": value
    }

# ---------------------------------------------------------
# Explicit / Known Sequence Payloads
# ---------------------------------------------------------

def active_player_set(game_id: str, account_id: str) -> Dict[str, Any]:
    return _build_msg(OutboundMsg.ACTIVE_PLAYER_SET.value, {
        "gameID": game_id,
        "accountID": account_id
    })

def opponent_picking_heads_or_tails(game_id: str, caller_id: str, prompt_id: int = 16, buttons: List[int] | None = None) -> Dict[str, Any]:
    return _build_msg(OutboundMsg.OBSERVER_CUSTOM_CHOICE_OFFER_MESSAGE.value, {
        "gameID": game_id,
        "selectingPlayer": caller_id,
        "prompt": {"id": prompt_id},
        "buttons": [{"id": b} for b in (buttons or [10, 11])],
        "offerLength": 30000,
        "sourceEntity": "00000000-0000-0000-0000-000000000000"
    })

def initial_coin_flip(game_id: str, actual_result: int, caller_entity_id: str, 
                      title_id: int = 18, game_text_id: int = 0) -> Dict[str, Any]:
    return _build_msg(OutboundMsg.MULTIPLE_COIN_FLIP_WITH_CONTEXT_EFFECT.value, {
        "gameID": game_id,
        "resultLst": [actual_result],
        "title": {"id": title_id},
        "gameText": {"id": game_text_id},
        "source": caller_entity_id,
        "targets": [caller_entity_id],
        "createTemporaryEffect": False
    })

# ---------------------------------------------------------
# Generic Sequence Helpers
# ---------------------------------------------------------
# For all other sequences, the client accepts standard game messages 
# (e.g. EntityMoved, AttributeModified) wrapped in the sequence block.
# We provide stub methods that wrap standard message parameters.

def recursive_return_to_owners_hand(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def reveal_mulligans(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def always_reveal(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def replace_active(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def simultaneous_flip_then_action(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def transform_entity(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def wonder_lock(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def deal_initial_hands(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def devolve(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def discard_retreat_cost(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def robo_substitute(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def flip_to_wake_up(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def with_open_prize_cards(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def burn_damage(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def bench_size_modified(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def create_legend(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def draw(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def flip_for_burn(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def flip_for_confusion(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def use_stadium_ability(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def play_card(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def hurt_from_confusion(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def introduce_initial_pokemon(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def grouped_move(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def attack(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def opponent_choosing_to_go_first(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def trainer_card(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def poke_ability(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def remove_special_condition(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def add_special_condition(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def mulligan(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def draw_prize_card(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def poison_damage(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def deal_initial_prize_cards(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def initial_pick(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def knockout(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def play_active(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def play_energy(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def play_tool(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def retreat(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def stadium_present(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def trainer_present(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def move_from_bottom_of_deck(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def move_from_middle_of_deck(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def move_from_top_of_deck(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def attach_to_vunion(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def close_prize_pile(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def dismiss_ability_select(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def parallel_sequence(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def reveal_and_skip_move(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def serial_sequence(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def vunion_break_sequence(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def create_vunion(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def active_card_and_attachments_shuffled(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def hand_shuffled_and_moved_to_deck(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)

def transform_swap(msg_name: str, **kwargs) -> Dict[str, Any]:
    return _build_msg(msg_name, kwargs)
