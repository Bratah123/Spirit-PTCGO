from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.session.effects import is_basic_pokemon

card = StadiumCardDef(
    passive=takes_less_passive(20, protects=lambda target, carrier: is_basic_pokemon(target)),
    guid="289a9041-9356-56a0-9fbe-d229afa1462f",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CirchesterBath.Name",
    display_name="Circhester Bath",
    searchable_by=["Circhester Bath", "Stadium"],
    subtypes=["Stadium"],
    collector_number=150,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
)
