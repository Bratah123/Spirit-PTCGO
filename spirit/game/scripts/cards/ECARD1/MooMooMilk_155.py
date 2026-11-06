from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.ecard import (
    moomoo_milk,
)

card = ItemCardDef(
    guid="6a320f3f-f2e9-5e37-8a41-2ef643856749",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MooMooMilk.Name",
    display_name="Moo-Moo Milk",
    searchable_by=["Moo-Moo Milk"],
    subtypes=[],
    collector_number=155,
    set_code="ECARD1",
    rarity=Rarities.Common,
    effect=moomoo_milk
)
