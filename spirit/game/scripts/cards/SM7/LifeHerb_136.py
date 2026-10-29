from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    life_herb,
    life_herb_condition,
)

card = ItemCardDef(
    guid="5ade656e-cffc-5c88-8aa0-0db74ad4c167",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=136,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=life_herb,
    condition=life_herb_condition,
)
