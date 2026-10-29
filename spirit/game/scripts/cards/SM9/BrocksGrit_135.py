from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    brocks_grit,
    brocks_grit_condition,
)

card = SupporterCardDef(
    guid="9754b007-d18c-5bb8-9841-225b9bfccc4f",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=brocks_grit,
            condition=brocks_grit_condition,
        )
