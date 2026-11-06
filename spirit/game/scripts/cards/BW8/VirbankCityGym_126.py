from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class VirbankCityGymPassive(Passive):
    """Put 2 more damage counters on Poisoned Pokemon (both sides) between turns."""

    def modify_poison_counters(self, counters, pokemon, carrier):
        return counters + 2


card = StadiumCardDef(
    guid="05a72a5d-eebf-5d02-b466-482575223882",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VirbankCityGym.Name",
    display_name="Virbank City Gym",
    searchable_by=["Virbank City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=126,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    passive=VirbankCityGymPassive()
)
