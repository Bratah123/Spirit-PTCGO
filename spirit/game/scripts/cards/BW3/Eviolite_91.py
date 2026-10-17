from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import AttrID, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.session.passives import carrier_pokemon


def _basic_holder(target, carrier):
    if carrier_pokemon(carrier) is not target:
        return False
    return target.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value


card = PokemonToolCardDef(
    guid="f975ed78-41cc-5739-9a23-c063368516d7",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eviolite.Name",
    display_name="Eviolite",
    searchable_by=["Eviolite", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=91,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(20, protects=_basic_holder),
)
