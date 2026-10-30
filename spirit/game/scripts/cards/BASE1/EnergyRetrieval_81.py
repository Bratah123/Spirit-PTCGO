from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0b0dab82-1de7-59c4-8e6e-4b2aa650f8ac",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval"],
    subtypes=[],
    collector_number=81,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_basic_energy_card),
    effect=recover_from_discard(is_basic_energy_card, count=2, minimum=1, to="hand"),
)
