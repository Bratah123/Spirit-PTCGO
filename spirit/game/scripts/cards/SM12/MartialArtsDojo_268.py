from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    martial_arts_dojo_passive,
)

card = StadiumCardDef(
    guid="30472cd5-8572-59ff-b99d-2a300a204f13",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MartialArtsDojo.Name",
    display_name="Martial Arts Dojo",
    searchable_by=["Martial Arts Dojo", "Stadium"],
    subtypes=["Stadium"],
    collector_number=268,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    passive=martial_arts_dojo_passive
)
