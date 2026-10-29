from spirit.game.card_effects.trainers import hand_size_at_least, ultra_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="40df68ee-6f56-55a6-b43b-d873c1301986",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=ultra_ball,
    condition=hand_size_at_least(3)
)
