from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least, ultra_ball

card = ItemCardDef(
    guid="9c213040-d91d-5c46-adea-10316aaacebf",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="BW9",
    rarity=Rarities.RareSecret,
    effect=ultra_ball,
    condition=hand_size_at_least(3)
)
