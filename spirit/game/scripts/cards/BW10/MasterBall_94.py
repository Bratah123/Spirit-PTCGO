from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


def _deck_not_empty(board, player_id, card=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = ItemCardDef(
    guid="c44dca6a-27da-56f3-89bc-3e49607496ea",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=94,
    set_code="BW10",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=search_to_hand(is_pokemon_card, count=1, minimum=0, reveal=True, prompt="Choose a Pokémon"),
    condition=_deck_not_empty
)
