from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import TRAINING_COURT_ABILITY

card = StadiumCardDef(
    guid="8fb314ca-2d3d-5117-a5bd-573d2d67bd15",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainingCourt.Name",
    display_name="Training Court",
    searchable_by=["Training Court", "Stadium"],
    subtypes=["Stadium"],
    collector_number=282,
    set_code="SWSH8",
    rarity=Rarities.RareSecret,
    ability=TRAINING_COURT_ABILITY,
)
