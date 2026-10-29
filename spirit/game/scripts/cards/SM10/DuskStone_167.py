from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    dusk_stone,
    dusk_stone_condition,
)

card = ItemCardDef(
    guid="583fe190-63d2-51b2-b0cd-cab473610326",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskStone.Name",
    display_name="Dusk Stone",
    searchable_by=["Dusk Stone", "Item"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=dusk_stone_condition,
    effect=dusk_stone
)
