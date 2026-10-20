from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_team_plasma_pokemon


def _deck_not_empty(board, player_id, card=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = ItemCardDef(
    guid="1b3890d6-4786-5fe6-aa3e-8afc54ada2e2",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaBall.Name",
    display_name="Team Plasma Ball",
    searchable_by=["Team Plasma Ball", "Item", "Team Plasma"],
    subtypes=["Item", "Team Plasma"],
    collector_number=105,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_team_plasma_pokemon, count=1, minimum=0, reveal=True,
                          prompt="Choose a Team Plasma Pokémon"),
    condition=_deck_not_empty
)
