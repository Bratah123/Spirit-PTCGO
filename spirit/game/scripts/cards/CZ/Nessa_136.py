from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard, is_energy
from spirit.game.session.effects import is_water_pokemon


def is_water_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy(card) and PokemonTypes.WATER.value in types


def _nessa_predicate(card) -> bool:
    return is_water_pokemon(card) or is_water_energy_card(card)


card = SupporterCardDef(
    guid="910d43ac-a842-55d1-81b5-f09de43ee5d8",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nessa.Name",
    display_name="Nessa",
    searchable_by=["Nessa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=136,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    effect=recover_from_discard(
        _nessa_predicate, count=4, minimum=1, reveal=False, to="hand",
        prompt="Choose up to 4 Water Pokémon and Water Energy cards",
    ),
    condition=requires_discard(_nessa_predicate),
)
