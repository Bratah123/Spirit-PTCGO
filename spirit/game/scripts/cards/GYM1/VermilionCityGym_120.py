from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import vermilion_city_gym_passive


card = StadiumCardDef(
    guid="0760beea-88de-58bf-9526-3ebe4198398f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VermilionCityGym.Name",
    display_name="Vermilion City Gym",
    searchable_by=["Vermilion City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=120,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    passive=vermilion_city_gym_passive,
)
