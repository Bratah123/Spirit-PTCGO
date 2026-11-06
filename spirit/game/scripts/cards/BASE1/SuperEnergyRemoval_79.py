from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    super_energy_removal,
    super_energy_removal_condition,
)


card = ItemCardDef(
    guid="d6fb7dd9-912b-5b19-b73e-7cd907c300ac",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRemoval.Name",
    display_name="Super Energy Removal",
    searchable_by=["Super Energy Removal"],
    subtypes=[],
    collector_number=79,
    set_code="BASE1",
    rarity=Rarities.Rare,
    condition=super_energy_removal_condition,
    effect=super_energy_removal,
)
