from spirit.game.card_effects.trainers import hand_size_at_least, quick_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cdaf82a1-0150-5052-b1ee-eb3fbe5437b6",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuickBall.Name",
    display_name="Quick Ball",
    searchable_by=["Quick Ball", "Item"],
    subtypes=["Item"],
    collector_number=216,
    set_code="SWSH1",
    rarity=Rarities.RareSecret,
    effect=quick_ball,
    condition=hand_size_at_least(2)
)
