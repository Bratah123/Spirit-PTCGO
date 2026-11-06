from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="14f2bf5e-bc6c-5c61-b75d-69544763092f",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval"],
    subtypes=[],
    collector_number=110,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_basic_energy_card),
    effect=recover_from_discard(is_basic_energy_card, count=2, minimum=1, to="hand"),
)
