from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    moomoo_milk,
)

card = ItemCardDef(
    guid="18c207d0-88ff-551a-a391-add93b936b6d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoomooMilk.Name",
    display_name="Moomoo Milk",
    searchable_by=["Moomoo Milk", "Item"],
    subtypes=["Item"],
    collector_number=185,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=moomoo_milk
)
