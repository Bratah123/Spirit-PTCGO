"""Roseanne's Research (POP8 #11)."""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_basic_pokemon


def _basic_pokemon_or_basic_energy(card):
    return is_basic_pokemon(card) or is_basic_energy_card(card)


card = SupporterCardDef(
    guid="9c0d1a53-c416-502a-bec0-382d1b0e89a8",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoseannesResearch.Name",
    display_name="Roseanne's Research",
    searchable_by=["Roseanne's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=11,
    set_code="POP8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _basic_pokemon_or_basic_energy, count=2, minimum=0, reveal=True,
        prompt="Choose up to 2 Basic Pokémon and/or basic Energy cards",
    ),
)
