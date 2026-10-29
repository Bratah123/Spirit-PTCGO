from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    LIFE_FOREST_ABILITY,
    stadium_lock_passive,
)

card = StadiumCardDef(
    guid="ad690ba9-8bfe-51d9-940a-38035f427dd5",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeForestPrismStar.Name",
    display_name="Life Forest {*}",
    searchable_by=["Life Forest {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=180,
    set_code="SM8",
    rarity=Rarities.Prism,
    ability=LIFE_FOREST_ABILITY,
    passive=stadium_lock_passive,
)
