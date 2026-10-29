from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    bills_maintenance,
    bills_maintenance_condition,
)

card = SupporterCardDef(
    guid="7d12bfa5-bb81-5ef2-a381-10b96cf6afeb",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=162,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=bills_maintenance,
    condition=bills_maintenance_condition,
)
