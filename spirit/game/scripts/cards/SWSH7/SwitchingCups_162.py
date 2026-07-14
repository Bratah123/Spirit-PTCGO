from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import primate_wisdom
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import deck_nonempty


def _switching_cups_condition(board, player_id, pokemon=None):
    return requires_hand(n=1)(board, player_id) and deck_nonempty(board, player_id)


card = ItemCardDef(
    guid="fbfb10ea-a91c-56a4-966d-3aea13668aa9",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwitchingCups.Name",
    display_name="Switching Cups",
    searchable_by=["Switching Cups", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    effect=primate_wisdom,
    condition=_switching_cups_condition,
)
