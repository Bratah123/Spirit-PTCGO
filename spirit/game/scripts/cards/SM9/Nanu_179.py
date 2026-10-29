from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    nanu,
    nanu_condition,
)

card = SupporterCardDef(
    guid="6663cb21-4d5e-5fd4-b1c6-d4ca4913a512",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nanu.Name",
    display_name="Nanu",
    searchable_by=["Nanu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=nanu,
            condition=nanu_condition,
        )
