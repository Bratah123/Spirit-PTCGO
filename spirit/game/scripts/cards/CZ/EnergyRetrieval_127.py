from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="41cc2388-5175-5545-bc15-ccee5bb21463",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="CZ",
    rarity=Rarities.Common,
    condition=requires_discard(is_basic_energy_card),
    effect=recover_from_discard(is_basic_energy_card, count=2, minimum=1, to="hand"),
)
