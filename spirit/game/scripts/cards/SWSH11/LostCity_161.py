from spirit.game.card_effects.trainers import LostCityPassive
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    passive=LostCityPassive(),
    guid="66e5b17d-fc88-5ccc-8aac-0f241db14f73",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostCity.Name",
    display_name="Lost City",
    searchable_by=["Lost City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=161,
    set_code="SWSH11",
    rarity=Rarities.Uncommon
)
