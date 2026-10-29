from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    martial_arts_dojo_passive,
)

card = StadiumCardDef(
    guid="5514f80a-20a0-578b-97d2-aff6b78b15c6",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MartialArtsDojo.Name",
    display_name="Martial Arts Dojo",
    searchable_by=["Martial Arts Dojo", "Stadium"],
    subtypes=["Stadium"],
    collector_number=179,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=martial_arts_dojo_passive
)
