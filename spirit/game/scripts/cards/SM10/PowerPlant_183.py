from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    power_plant_passive,
)

card = StadiumCardDef(
    guid="247b5520-cbb1-5b07-8890-00e4bf8b64a4",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name",
    display_name="Power Plant",
    searchable_by=["Power Plant", "Stadium"],
    subtypes=["Stadium"],
    collector_number=183,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=power_plant_passive
)
