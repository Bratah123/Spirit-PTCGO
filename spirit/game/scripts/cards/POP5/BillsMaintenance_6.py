from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import bills_maintenance

card = SupporterCardDef(
    guid="aa263c20-d33e-5415-b30f-d2068972a541",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=6,
    set_code="POP5",
    rarity=Rarities.Uncommon,
    effect=bills_maintenance,
)
