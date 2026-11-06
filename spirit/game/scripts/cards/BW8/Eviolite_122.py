from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import AttrID, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.session.passives import carrier_pokemon


def _basic_holder(target, carrier):
    if carrier_pokemon(carrier) is not target:
        return False
    return target.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value


card = PokemonToolCardDef(
    guid="f12b4481-2161-555d-83ee-288d7d417128",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eviolite.Name",
    display_name="Eviolite",
    searchable_by=["Eviolite", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(20, protects=_basic_holder),
)
