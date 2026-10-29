from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import order_pad

card = ItemCardDef(
    guid="ea39c280-408d-597b-9a7d-d7586e5ea8e2",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OrderPad.Name",
    display_name="Order Pad",
    searchable_by=["Order Pad", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=order_pad,
)
