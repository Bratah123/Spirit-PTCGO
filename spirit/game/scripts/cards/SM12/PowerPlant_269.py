from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    power_plant_passive,
)

card = StadiumCardDef(
    guid="e8a68e1d-2d9b-5b51-8acc-21cdd274776a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name",
    display_name="Power Plant",
    searchable_by=["Power Plant", "Stadium"],
    subtypes=["Stadium"],
    collector_number=269,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    passive=power_plant_passive
)
