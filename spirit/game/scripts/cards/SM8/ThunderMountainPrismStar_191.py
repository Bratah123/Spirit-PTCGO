from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    thunder_mountain_passive,
)

card = StadiumCardDef(
    guid="1485ad3a-47aa-5606-bf5c-8f4df4389ca2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThunderMountainPrismStar.Name",
    display_name="Thunder Mountain {*}",
    searchable_by=["Thunder Mountain {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=191,
    set_code="SM8",
    rarity=Rarities.Prism,
    passive=thunder_mountain_passive,
)
