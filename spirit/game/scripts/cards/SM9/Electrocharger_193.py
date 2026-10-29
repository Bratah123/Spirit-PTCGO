from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    electrocharger,
    electrocharger_condition,
)

card = ItemCardDef(
    guid="78af3a11-93d0-541a-a3ac-5c7b59eda215",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electrocharger.Name",
    display_name="Electrocharger",
    searchable_by=["Electrocharger", "Item"],
    subtypes=["Item"],
    collector_number=193,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    effect=electrocharger,
            condition=electrocharger_condition,
        )
