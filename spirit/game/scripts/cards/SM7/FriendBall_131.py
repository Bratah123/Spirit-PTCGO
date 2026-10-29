from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    friend_ball,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="37bc31bf-b9da-5c15-b5bf-f8e0d25aead8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendBall.Name",
    display_name="Friend Ball",
    searchable_by=["Friend Ball", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=friend_ball,
    condition=deck_nonempty,
)
