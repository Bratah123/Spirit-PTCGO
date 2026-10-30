from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import bills_maintenance

card = SupporterCardDef(
    guid="68a66fad-1440-5aec-aba0-6856f397b463",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=71,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=bills_maintenance,
)
