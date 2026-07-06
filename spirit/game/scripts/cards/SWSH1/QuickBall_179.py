from spirit.game.card_effects.trainers import hand_size_at_least, quick_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="252c66c6-ce03-5018-b260-b8f7bfe4909d",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuickBall.Name",
    display_name="Quick Ball",
    searchable_by=["Quick Ball", "Item"],
    subtypes=["Item"],
    collector_number=179,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=quick_ball,
    condition=hand_size_at_least(2)
)
