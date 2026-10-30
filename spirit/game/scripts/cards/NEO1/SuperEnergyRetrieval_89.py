from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    super_energy_retrieval,
    super_energy_retrieval_condition,
)


card = ItemCardDef(
    guid="0d7c1281-b3da-5ce6-b7eb-1100930f7ad2",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRetrieval.Name",
    display_name="Super Energy Retrieval",
    searchable_by=["Super Energy Retrieval"],
    subtypes=[],
    collector_number=89,
    set_code="NEO1",
    rarity=Rarities.Rare,
    condition=super_energy_retrieval_condition,
    effect=super_energy_retrieval,
)
