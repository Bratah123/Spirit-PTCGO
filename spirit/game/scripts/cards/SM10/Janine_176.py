from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    janine,
)

card = SupporterCardDef(
    guid="25628850-e253-5e25-a7d8-9282c01c76af",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Janine.Name",
    display_name="Janine",
    searchable_by=["Janine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=janine
)
