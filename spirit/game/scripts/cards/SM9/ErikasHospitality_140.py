from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    erikas_hospitality,
    erikas_hospitality_condition,
)

card = SupporterCardDef(
    guid="f7eb4870-efd0-5bc8-8935-276dd4c90248",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasHospitality.Name",
    display_name="Erika's Hospitality",
    searchable_by=["Erika's Hospitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    effect=erikas_hospitality,
            condition=erikas_hospitality_condition,
        )
