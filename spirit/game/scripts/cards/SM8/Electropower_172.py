from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    electropower,
)

card = ItemCardDef(
    guid="ecd02bff-1f02-5744-a64a-fdc1387d71da",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electropower.Name",
    display_name="Electropower",
    searchable_by=["Electropower", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=electropower
)
