from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    surprise_box,
    surprise_box_condition,
)

card = ItemCardDef(
    guid="9c5d0692-2693-5f40-8d83-cdc30271655c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurpriseBox.Name",
    display_name="Surprise Box",
    searchable_by=["Surprise Box", "Item"],
    subtypes=["Item"],
    collector_number=187,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=surprise_box_condition,
    effect=surprise_box
)
