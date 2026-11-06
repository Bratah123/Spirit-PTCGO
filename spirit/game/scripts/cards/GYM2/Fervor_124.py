from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import fervor, has_cards_in_deck


card = ItemCardDef(
    guid="952e2151-0c0c-5086-8a5d-323e6e1cdc2a",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fervor.Name",
    display_name="Fervor",
    searchable_by=["Fervor"],
    subtypes=[],
    collector_number=124,
    set_code="GYM2",
    rarity=Rarities.Common,
    condition=has_cards_in_deck,
    effect=fervor,
)
