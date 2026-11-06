from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.ecard import has_cards_in_deck

card = ItemCardDef(
    guid="4a4961ac-af79-5067-b52d-be88935b48b8",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name",
    display_name="Bill",
    searchable_by=["Bill"],
    subtypes=[],
    collector_number=91,
    set_code="BASE1",
    rarity=Rarities.Common,
    condition=has_cards_in_deck,
    effect=draw_attack(2)
)
