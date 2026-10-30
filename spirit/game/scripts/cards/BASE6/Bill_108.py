from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.ecard import has_cards_in_deck

card = ItemCardDef(
    guid="bfc1af0c-ff99-5130-a3f7-89387834cd69",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name",
    display_name="Bill",
    searchable_by=["Bill"],
    subtypes=[],
    collector_number=108,
    set_code="BASE6",
    rarity=Rarities.Common,
    condition=has_cards_in_deck,
    effect=draw_attack(2)
)
