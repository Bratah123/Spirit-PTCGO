from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


def fisherman_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_basic_energy_card(c) for c in discard.children)


card = SupporterCardDef(
    guid="3e6a37da-7286-5304-b7d5-41a369fa2e9a",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=136,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=4, minimum=4, reveal=True,
                                prompt="Choose 4 basic Energy cards"),
    condition=fisherman_condition
)
