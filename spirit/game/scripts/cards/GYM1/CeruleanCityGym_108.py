from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import gym_owner
from spirit.game.card_effects.passives_common import retreat_discount


card = StadiumCardDef(
    guid="b06ff56d-2204-5fec-84a3-4398d36e4545",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeruleanCityGym.Name",
    display_name="Cerulean City Gym",
    searchable_by=["Cerulean City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=108,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    passive=retreat_discount(1, gym_owner("Misty")),
)
