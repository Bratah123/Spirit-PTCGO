from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import ULTRA_SPACE_ABILITY

card = StadiumCardDef(
    guid="275ec1de-d82c-5643-8416-eb4529477822",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraSpace.Name",
    display_name="Ultra Space",
    searchable_by=["Ultra Space", "Stadium"],
    subtypes=["Stadium"],
    collector_number=115,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    ability=ULTRA_SPACE_ABILITY,
)
