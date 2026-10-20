from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.card_effects.passives_common import condition_immunity_passive


def _metal(target, carrier):
    return PokemonTypes.METAL.value in (target.get_attribute(AttrID.POKEMON_TYPES) or [])


card = StadiumCardDef(
    guid="32608b93-6a75-5185-88d7-2e7ab660357d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SteelShelter.Name",
    display_name="Steel Shelter",
    searchable_by=["Steel Shelter", "Stadium"],
    subtypes=["Stadium"],
    collector_number=105,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=condition_immunity_passive(protects=_metal)
)
