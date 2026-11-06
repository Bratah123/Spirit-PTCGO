from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import mistys_wish, mistys_wish_condition


card = ItemCardDef(
    guid="8a3bf543-6627-5e5f-9529-cf757595acee",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysWish.Name",
    display_name="Misty's Wish",
    searchable_by=["Misty's Wish"],
    subtypes=[],
    collector_number=108,
    set_code="GYM2",
    rarity=Rarities.Rare,
    condition=mistys_wish_condition,
    effect=mistys_wish,
)
