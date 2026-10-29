from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    mina,
)

card = SupporterCardDef(
    guid="c94e3145-336b-5f21-b872-42b564179c00",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mina.Name",
    display_name="Mina",
    searchable_by=["Mina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=183,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=mina
)
