from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    super_energy_removal,
    super_energy_removal_condition,
)


card = ItemCardDef(
    guid="d432f18b-0bce-5d88-bdff-fc4838071e09",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRemoval.Name",
    display_name="Super Energy Removal",
    searchable_by=["Super Energy Removal"],
    subtypes=[],
    collector_number=108,
    set_code="BASE4",
    rarity=Rarities.Rare,
    condition=super_energy_removal_condition,
    effect=super_energy_removal,
)
