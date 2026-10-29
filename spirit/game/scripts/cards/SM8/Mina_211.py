from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    mina,
)

card = SupporterCardDef(
    guid="e29f2542-6657-5fb2-9244-0cfb4b627166",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mina.Name",
    display_name="Mina",
    searchable_by=["Mina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=211,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    effect=mina
)
