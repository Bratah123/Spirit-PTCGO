from spirit.game.card_effects.trainers import hand_size_at_least, ultra_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a0d4b655-f3bb-563c-b9c1-79ea425d7a65",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SM1",
    rarity=Rarities.RareSecret,
    effect=ultra_ball,
    condition=hand_size_at_least(3)
)
