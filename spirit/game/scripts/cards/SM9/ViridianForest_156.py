from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    VIRIDIAN_FOREST_ABILITY,
)

card = StadiumCardDef(
    guid="703e2173-f13f-50ed-9daf-9878cfb83ddc",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianForest.Name",
    display_name="Viridian Forest",
    searchable_by=["Viridian Forest", "Stadium"],
    subtypes=["Stadium"],
    collector_number=156,
    set_code="SM9",
    rarity=Rarities.Uncommon,
            ability=VIRIDIAN_FOREST_ABILITY,
        )
