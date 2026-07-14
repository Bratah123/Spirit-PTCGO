from spirit.game.card_effects.trainers import hand_size_at_least, ultra_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="adfa2e63-35ba-5d3c-96cc-9d01e1b779f8",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=ultra_ball,
    condition=hand_size_at_least(3)
)
