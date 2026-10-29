from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import rosa, rosa_condition

card = SupporterCardDef(
    guid="e2e69de4-d96f-5c7c-bb49-5585d70bc83d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rosa.Name",
    display_name="Rosa",
    searchable_by=["Rosa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    effect=rosa, condition=rosa_condition,
)
