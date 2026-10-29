from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    last_chance_potion,
    last_chance_potion_condition,
)

card = ItemCardDef(
    guid="ae195811-c19a-598c-97b5-c879564382f6",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LastChancePotion.Name",
    display_name="Last Chance Potion",
    searchable_by=["Last Chance Potion", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=last_chance_potion,
    condition=last_chance_potion_condition,
)
