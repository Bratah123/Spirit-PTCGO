from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    electromagnetic_radar,
    electromagnetic_radar_condition,
)

card = ItemCardDef(
    guid="ec5d5ca1-5657-5a33-9f80-59e78075246c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectromagneticRadar.Name",
    display_name="Electromagnetic Radar",
    searchable_by=["Electromagnetic Radar", "Item"],
    subtypes=["Item"],
    collector_number=169,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=electromagnetic_radar_condition,
    effect=electromagnetic_radar
)
