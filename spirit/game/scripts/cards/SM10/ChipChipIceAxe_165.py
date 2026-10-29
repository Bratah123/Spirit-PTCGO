from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    chip_chip_ice_axe,
)

card = ItemCardDef(
    guid="06f9d510-ef03-5437-b9bd-5f1e0cfa3d77",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChipChipIceAxe.Name",
    display_name="Chip-Chip Ice Axe",
    searchable_by=["Chip-Chip Ice Axe", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=chip_chip_ice_axe
)
