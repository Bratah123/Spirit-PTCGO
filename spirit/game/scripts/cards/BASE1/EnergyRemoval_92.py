from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import energy_removal
from spirit.game.card_effects.trainers import opponent_has_energy_attached


card = ItemCardDef(
    guid="ba29102d-bffa-50fc-9029-2423e5d1772b",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval.Name",
    display_name="Energy Removal",
    searchable_by=["Energy Removal"],
    subtypes=[],
    collector_number=92,
    set_code="BASE1",
    rarity=Rarities.Common,
    condition=opponent_has_energy_attached,
    effect=energy_removal,
)
