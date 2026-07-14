from spirit.game.card_effects.trainers import quad_stone
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="eeebbfa7-376f-5c26-96f9-46c4478943ee",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuadStone.Name",
    display_name="Quad Stone",
    searchable_by=["Quad Stone", "Item"],
    subtypes=["Item"],
    collector_number=163,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    effect=quad_stone
)
