from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.hf import brocks_pewter_city_gym_passive

card = StadiumCardDef(
    guid="f9b480aa-f3b2-5e27-95aa-b816005f0e33",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksPewterCityGym.Name",
    display_name="Brock's Pewter City Gym",
    searchable_by=["Brock's Pewter City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=54,
    set_code="HF",
    rarity=Rarities.Uncommon,
    passive=brocks_pewter_city_gym_passive,
)
