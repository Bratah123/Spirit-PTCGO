from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    devolution_spray_z,
    devolution_spray_z_condition,
)

card = ItemCardDef(
    guid="cd6aad16-2ac2-5568-a8d3-098477c3d15d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSprayZ.Name",
    display_name="Devolution Spray Z",
    searchable_by=["Devolution Spray Z", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=devolution_spray_z_condition,
    effect=devolution_spray_z
)
