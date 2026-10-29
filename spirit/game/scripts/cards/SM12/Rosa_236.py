from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import rosa, rosa_condition

card = SupporterCardDef(
    guid="24d620d6-8e86-54fe-a953-09d2af8d8672",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rosa.Name",
    display_name="Rosa",
    searchable_by=["Rosa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=236,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=rosa, condition=rosa_condition,
)
