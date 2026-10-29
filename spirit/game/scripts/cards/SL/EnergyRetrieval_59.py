from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fa06319a-dc76-524f-bade-fc0265d7ad35",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=59,
    set_code="SL",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_basic_energy_card),
    effect=recover_from_discard(is_basic_energy_card, count=2, minimum=1, to="hand"),
)
