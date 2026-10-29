from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    electromagnetic_radar,
    electromagnetic_radar_condition,
)

card = ItemCardDef(
    guid="d91e92fc-a188-52af-910d-c2d639f7d86f",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectromagneticRadar.Name",
    display_name="Electromagnetic Radar",
    searchable_by=["Electromagnetic Radar", "Item"],
    subtypes=["Item"],
    collector_number=230,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    condition=electromagnetic_radar_condition,
    effect=electromagnetic_radar
)
