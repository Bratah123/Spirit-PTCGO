from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.session.effects import is_basic_pokemon


def _aether_protects(target, carrier):
    if not is_basic_pokemon(target):
        return False
    types = target.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.GRASS.value in types or PokemonTypes.LIGHTNING.value in types


card = StadiumCardDef(
    guid="9b047b0c-08d7-59a2-9c03-dcf509f6f918",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherParadiseConservationArea.Name",
    display_name="Aether Paradise Conservation Area",
    searchable_by=["Aether Paradise Conservation Area", "Stadium"],
    subtypes=["Stadium"],
    collector_number=116,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(30, protects=_aether_protects),
)
