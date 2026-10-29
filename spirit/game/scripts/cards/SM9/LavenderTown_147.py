from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    LAVENDER_TOWN_ABILITY,
)

card = StadiumCardDef(
    guid="6a6dbfa1-4f6d-5511-82d2-6a709d43bb5d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LavenderTown.Name",
    display_name="Lavender Town",
    searchable_by=["Lavender Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=147,
    set_code="SM9",
    rarity=Rarities.Uncommon,
            ability=LAVENDER_TOWN_ABILITY,
        )
