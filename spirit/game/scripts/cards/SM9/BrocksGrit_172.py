from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    brocks_grit,
    brocks_grit_condition,
)

card = SupporterCardDef(
    guid="76a5e6ca-7405-5fcb-9e4d-29d4da35c255",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=172,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=brocks_grit,
            condition=brocks_grit_condition,
        )
