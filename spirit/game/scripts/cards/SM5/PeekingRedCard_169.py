from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import peeking_red_card

card = ItemCardDef(
    guid="a6084b29-e8d0-5287-93c4-1d2c316dfec4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name",
    display_name="Peeking Red Card",
    searchable_by=["Peeking Red Card", "Item"],
    subtypes=["Item"],
    collector_number=169,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    effect=peeking_red_card,
)
