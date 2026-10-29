from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import mysterious_treasure, mysterious_treasure_condition

card = ItemCardDef(
    guid="e4c0fe58-9836-570d-8aa9-22fd1452d245",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousTreasure.Name",
    display_name="Mysterious Treasure",
    searchable_by=["Mysterious Treasure", "Item"],
    subtypes=["Item"],
    collector_number=113,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    condition=mysterious_treasure_condition,
    effect=mysterious_treasure,
)
