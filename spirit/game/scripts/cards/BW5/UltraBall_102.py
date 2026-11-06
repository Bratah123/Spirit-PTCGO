from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least, ultra_ball

card = ItemCardDef(
    guid="59accf12-b9ad-5869-b8cc-4fe46dc3f3f3",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=ultra_ball,
    condition=hand_size_at_least(3)
)
