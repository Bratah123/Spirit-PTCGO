from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import mysterious_treasure, mysterious_treasure_condition

card = ItemCardDef(
    guid="b598c5db-dd31-562b-a498-4d88c5a2aed3",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousTreasure.Name",
    display_name="Mysterious Treasure",
    searchable_by=["Mysterious Treasure", "Item"],
    subtypes=["Item"],
    collector_number=145,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    condition=mysterious_treasure_condition,
    effect=mysterious_treasure,
)
