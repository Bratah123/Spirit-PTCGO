from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_water_energy(card):
    return is_basic_energy_card(card) and PokemonTypes.WATER.value in (
        card.get_attribute(AttrID.POKEMON_TYPES) or []
    )


card = ItemCardDef(
    guid="16d1e917-da92-5a04-ba26-e703abff008e",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CapaciousBucket.Name",
    display_name="Capacious Bucket",
    searchable_by=["Capacious Bucket", "Item"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _is_water_energy, count=2, minimum=0, reveal=True,
        prompt="Choose up to 2 Water Energy cards.",
    )
)
