from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import MountLanakilaPassive

card = StadiumCardDef(
    guid="80e89095-915b-574b-bdd4-5bc875641b9f",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MountLanakila.Name",
    display_name="Mount Lanakila",
    searchable_by=["Mount Lanakila", "Stadium"],
    subtypes=["Stadium"],
    collector_number=118,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    passive=MountLanakilaPassive(),)
