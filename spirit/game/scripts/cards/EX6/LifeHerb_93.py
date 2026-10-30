from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import life_herb

card = ItemCardDef(
    guid="25f92163-6207-523b-83fc-4811270e30b4",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=life_herb,
)
