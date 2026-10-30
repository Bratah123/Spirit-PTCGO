from spirit.game.card_effects.trainers import hand_size_at_least, quick_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f90c74cc-600a-5197-a31e-bb06f32abf7f",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuickBall.Name",
    display_name="Quick Ball",
    searchable_by=["Quick Ball", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=quick_ball,
    condition=hand_size_at_least(2)
)
