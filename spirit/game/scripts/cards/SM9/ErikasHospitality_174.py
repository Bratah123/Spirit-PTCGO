from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    erikas_hospitality,
    erikas_hospitality_condition,
)

card = SupporterCardDef(
    guid="3ab9af14-c5d5-5b86-8d07-acbc15d60217",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasHospitality.Name",
    display_name="Erika's Hospitality",
    searchable_by=["Erika's Hospitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=erikas_hospitality,
            condition=erikas_hospitality_condition,
        )
