from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import peeking_red_card

card = ItemCardDef(
    guid="b818ec09-ef33-5424-bd54-16aa869707a6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name",
    display_name="Peeking Red Card",
    searchable_by=["Peeking Red Card", "Item"],
    subtypes=["Item"],
    collector_number=97,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=peeking_red_card,
)
