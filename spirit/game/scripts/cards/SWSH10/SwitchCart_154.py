from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch_cart, switch_cart_condition

card = ItemCardDef(
    guid="55815436-e040-5f89-9194-0791b6ff5671",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwitchCart.Name",
    display_name="Switch Cart",
    searchable_by=["Switch Cart", "Item"],
    subtypes=["Item"],
    collector_number=154,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    condition=switch_cart_condition,
    effect=switch_cart,
)
