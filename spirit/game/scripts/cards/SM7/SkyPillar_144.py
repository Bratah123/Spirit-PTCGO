from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    sky_pillar_passive,
)

card = StadiumCardDef(
    guid="6b6b2fa4-989e-5220-9ea1-5610e33a303e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyPillar.Name",
    display_name="Sky Pillar",
    searchable_by=["Sky Pillar", "Stadium"],
    subtypes=["Stadium"],
    collector_number=144,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    passive=sky_pillar_passive,
)
