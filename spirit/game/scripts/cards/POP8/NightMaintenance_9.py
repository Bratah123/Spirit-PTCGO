"""Night Maintenance (POP8 #9)."""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_pokemon_card


def _pokemon_or_basic_energy(card):
    return is_pokemon_card(card) or is_basic_energy_card(card)


card = ItemCardDef(
    guid="374c81d2-1510-53cc-9a38-c8e79ccb3896",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightMaintenance.Name",
    display_name="Night Maintenance",
    searchable_by=["Night Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="POP8",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(
        _pokemon_or_basic_energy, count=3, minimum=0, reveal=True,
        to="deck_shuffle",
        prompt="Choose up to 3 Pokémon and/or basic Energy cards",
    ),
)
