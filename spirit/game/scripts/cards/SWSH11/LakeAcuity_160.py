from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.passives_common import takes_less_passive


def _has_water_or_fighting_energy(pokemon) -> bool:
    return any(
        is_energy_card(c) and (
            energy_provides_type(c, PokemonTypes.WATER.value)
            or energy_provides_type(c, PokemonTypes.FIGHTING.value)
        )
        for c in pokemon.children
    )


card = StadiumCardDef(
    guid="a133e101-31d6-5ae1-96c2-85a0b1cfe759",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LakeAcuity.Name",
    display_name="Lake Acuity",
    searchable_by=["Lake Acuity", "Stadium"],
    subtypes=["Stadium"],
    collector_number=160,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(
        20, protects=lambda target, carrier: _has_water_or_fighting_energy(target)
    ),
)
