from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    brocks_grit,
    brocks_grit_condition,
)

card = SupporterCardDef(
    guid="9a9ff7e9-7328-5ce7-b42d-a99100c931d3",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=53,
    set_code="HF",
    rarity=Rarities.Uncommon,
    effect=brocks_grit,
            condition=brocks_grit_condition,
        )
