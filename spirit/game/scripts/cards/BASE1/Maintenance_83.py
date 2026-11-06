from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import maintenance, maintenance_condition


card = ItemCardDef(
    guid="637b0637-f28f-5e86-879f-a65742999194",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance"],
    subtypes=[],
    collector_number=83,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    condition=maintenance_condition,
    effect=maintenance,
)
