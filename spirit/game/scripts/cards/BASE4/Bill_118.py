from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.ecard import has_cards_in_deck

card = ItemCardDef(
    guid="87d14847-b7fb-5bac-a173-f4333188f321",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name",
    display_name="Bill",
    searchable_by=["Bill"],
    subtypes=[],
    collector_number=118,
    set_code="BASE4",
    rarity=Rarities.Common,
    condition=has_cards_in_deck,
    effect=draw_attack(2)
)
