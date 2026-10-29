from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import PoTownPassive

card = StadiumCardDef(
    guid="47e7adfc-ca5b-5eaf-ab1e-cf478e51515d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PoTown.Name",
    display_name="Po Town",
    searchable_by=["Po Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=121,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    passive=PoTownPassive(),)
