from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import search_to_hand


def _psychic_energy_or_basic(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.PSYCHIC.value not in types:
        return False
    return is_basic_energy_card(card) or is_basic_pokemon(card)


card = ItemCardDef(
    guid="bbdbfe30-0cb0-5d68-92c7-9fc784d29fe4",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FogCrystal.Name",
    display_name="Fog Crystal",
    searchable_by=["Fog Crystal", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _psychic_energy_or_basic, count=1, minimum=0, reveal=True,
        prompt="Choose a Psychic Energy card or a Basic Psychic Pokémon.",
    ),
)
