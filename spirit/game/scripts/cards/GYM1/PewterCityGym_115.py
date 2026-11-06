from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pewter_city_gym_passive


card = StadiumCardDef(
    guid="deb0626a-251f-5250-8e39-76750dd7d088",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PewterCityGym.Name",
    display_name="Pewter City Gym",
    searchable_by=["Pewter City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=115,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    passive=pewter_city_gym_passive,
)
