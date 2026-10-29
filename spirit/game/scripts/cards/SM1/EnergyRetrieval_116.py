from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b07084a7-ee5d-5f14-8008-f09d8fe5ee78",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_basic_energy_card),
    effect=recover_from_discard(is_basic_energy_card, count=2, minimum=1, to="hand"),
)
