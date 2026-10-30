from spirit.game.card_effects.trainers import hand_size_at_least, quick_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5f810ad0-d313-5637-9e24-dce7b700c9fd",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuickBall.Name",
    display_name="Quick Ball",
    searchable_by=["Quick Ball", "Item"],
    subtypes=["Item"],
    collector_number=114,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=quick_ball,
    condition=hand_size_at_least(2)
)
