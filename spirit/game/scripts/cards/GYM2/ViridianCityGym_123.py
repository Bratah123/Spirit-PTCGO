from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import viridian_city_gym_passive


card = StadiumCardDef(
    guid="ebf437b8-1aed-58a3-a919-6dcf794937d8",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianCityGym.Name",
    display_name="Viridian City Gym",
    searchable_by=["Viridian City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=123,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    passive=viridian_city_gym_passive,
)
