from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import mysterious_treasure, mysterious_treasure_condition

card = ItemCardDef(
    guid="2761d4f0-f0a0-56fc-8aed-90ffc37a4d80",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousTreasure.Name",
    display_name="Mysterious Treasure",
    searchable_by=["Mysterious Treasure", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    condition=mysterious_treasure_condition,
    effect=mysterious_treasure,
)
