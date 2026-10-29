from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    life_herb,
    life_herb_condition,
)

card = ItemCardDef(
    guid="bf702ca9-b6b6-5726-b53d-00fb3670569f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=180,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    effect=life_herb,
    condition=life_herb_condition,
)
