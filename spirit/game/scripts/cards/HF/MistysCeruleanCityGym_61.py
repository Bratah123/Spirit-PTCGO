from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.hf import mistys_cerulean_city_gym_passive

card = StadiumCardDef(
    guid="b418c08c-3243-5178-9945-39d37e5730f1",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysCeruleanCityGym.Name",
    display_name="Misty's Cerulean City Gym",
    searchable_by=["Misty's Cerulean City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=61,
    set_code="HF",
    rarity=Rarities.Uncommon,
    passive=mistys_cerulean_city_gym_passive,
)
