from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    fire_crystal,
)

card = ItemCardDef(
    guid="3e059737-81d7-5c70-89fb-9acba4c54819",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCrystal.Name",
    display_name="Fire Crystal",
    searchable_by=["Fire Crystal", "Item"],
    subtypes=["Item"],
    collector_number=231,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    effect=fire_crystal
)
