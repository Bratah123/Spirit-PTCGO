from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import chaotic_swell_passive

card = StadiumCardDef(
    guid="53ff5d70-7635-5aad-b190-be61c579151d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaoticSwell.Name",
    display_name="Chaotic Swell",
    searchable_by=["Chaotic Swell", "Stadium"],
    subtypes=["Stadium"],
    collector_number=187,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    passive=chaotic_swell_passive,
)
