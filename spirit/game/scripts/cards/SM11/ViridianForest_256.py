from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    VIRIDIAN_FOREST_ABILITY,
)

card = StadiumCardDef(
    guid="097a3578-7537-511d-b4ac-5993524d7b23",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianForest.Name",
    display_name="Viridian Forest",
    searchable_by=["Viridian Forest", "Stadium"],
    subtypes=["Stadium"],
    collector_number=256,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    ability=VIRIDIAN_FOREST_ABILITY,
)
