from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import retreat_discount
from spirit.game.session.effects import is_basic_pokemon

card = StadiumCardDef(
    guid="eef9d804-c6b4-51c2-bdfa-36e5d22b410b",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyarrowBridge.Name",
    display_name="Skyarrow Bridge",
    searchable_by=["Skyarrow Bridge", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    passive=retreat_discount(1, target_pred=lambda pokemon, carrier: is_basic_pokemon(pokemon))
)
