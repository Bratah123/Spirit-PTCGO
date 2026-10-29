from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    electrocharger,
    electrocharger_condition,
)

card = ItemCardDef(
    guid="39e9f59b-c13e-5f3c-ae47-dc6d8d834dd3",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electrocharger.Name",
    display_name="Electrocharger",
    searchable_by=["Electrocharger", "Item"],
    subtypes=["Item"],
    collector_number=139,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=electrocharger,
            condition=electrocharger_condition,
        )
