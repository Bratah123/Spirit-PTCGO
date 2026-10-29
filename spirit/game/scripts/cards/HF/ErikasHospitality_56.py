from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    erikas_hospitality,
    erikas_hospitality_condition,
)

card = SupporterCardDef(
    guid="85226b04-9e88-5572-b57a-3e3da3f50665",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasHospitality.Name",
    display_name="Erika's Hospitality",
    searchable_by=["Erika's Hospitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=56,
    set_code="HF",
    rarity=Rarities.Rare,
    effect=erikas_hospitality,
            condition=erikas_hospitality_condition,
        )
