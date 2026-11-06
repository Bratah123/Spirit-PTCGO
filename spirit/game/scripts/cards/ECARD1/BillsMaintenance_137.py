from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    bills_maintenance,
    bills_maintenance_condition,
)

card = SupporterCardDef(
    guid="004561a8-5f5d-50ed-bcca-f77946f3b105",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=bills_maintenance,
    condition=bills_maintenance_condition,
)
