from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import bills_maintenance

card = SupporterCardDef(
    guid="f93312cf-60e9-5de6-8804-e9b62e2403bf",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=bills_maintenance,
)
