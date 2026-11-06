from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import maintenance, maintenance_condition


card = ItemCardDef(
    guid="66adede1-9e5d-5255-9003-2fd6298d0c60",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance"],
    subtypes=[],
    collector_number=112,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    condition=maintenance_condition,
    effect=maintenance,
)
