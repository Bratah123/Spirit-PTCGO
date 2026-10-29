from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import no_weakness_passive


def _is_fire_or_metal(target, carrier):
    types = target.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types or PokemonTypes.METAL.value in types


card = StadiumCardDef(
    guid="28c092f5-d671-5e44-9cd2-70284abb38a9",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AltaroftheSunne.Name",
    display_name="Altar of the Sunne",
    searchable_by=["Altar of the Sunne", "Stadium"],
    subtypes=["Stadium"],
    collector_number=118,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=no_weakness_passive(protects=_is_fire_or_metal),
)
