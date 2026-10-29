from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    ultra_forest_kartenvoy,
    ultra_forest_kartenvoy_condition,
)

card = SupporterCardDef(
    guid="fe8c8dc0-70d8-5b82-a12b-981517ad54e0",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraForestKartenvoy.Name",
    display_name="Ultra Forest Kartenvoy",
    searchable_by=["Ultra Forest Kartenvoy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=ultra_forest_kartenvoy_condition,
    effect=ultra_forest_kartenvoy
)
