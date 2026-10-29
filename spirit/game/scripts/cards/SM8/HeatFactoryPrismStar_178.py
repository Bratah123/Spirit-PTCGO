from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    HEAT_FACTORY_ABILITY,
    stadium_lock_passive,
)

card = StadiumCardDef(
    guid="e1bd8637-68e3-5fa6-a2e6-bc09bae61021",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeatFactoryPrismStar.Name",
    display_name="Heat Factory {*}",
    searchable_by=["Heat Factory {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=178,
    set_code="SM8",
    rarity=Rarities.Prism,
    ability=HEAT_FACTORY_ABILITY,
    passive=stadium_lock_passive,
)
