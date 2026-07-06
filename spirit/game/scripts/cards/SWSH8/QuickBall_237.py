from spirit.game.card_effects.trainers import hand_size_at_least, quick_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="54ad8b77-0b99-52d7-a971-5a244f19f04e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuickBall.Name",
    display_name="Quick Ball",
    searchable_by=["Quick Ball", "Item"],
    subtypes=["Item"],
    collector_number=237,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=quick_ball,
    condition=hand_size_at_least(2)
)
