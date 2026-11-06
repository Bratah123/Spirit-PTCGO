from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import cinnabar_city_gym_passive


card = StadiumCardDef(
    guid="c6be19f3-4b3c-5811-a8c8-ebda04595583",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CinnabarCityGym.Name",
    display_name="Cinnabar City Gym",
    searchable_by=["Cinnabar City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=113,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    passive=cinnabar_city_gym_passive,
)
