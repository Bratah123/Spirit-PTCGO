"""Miracle Energy (NEO4 #16).

Card text:
  You can't have more than 1 Miracle Energy in your deck. Attach Miracle Energy
  to 1 of your Shining or Light Pokémon. At the end of your turn, discard
  Miracle Energy.
  While in play, Miracle Energy counts as every type of Energy but provides
  only 2 Energy at a time.
"""

from spirit.game.data_utils import Ability, EnergyCardDef, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, Rarities
from spirit.game.card_effects.energies import (
    ALL_TYPES_TWO_AT_A_TIME,
    attach_to_shining_or_light,
    discard_energy_end_of_turn,
)

card = EnergyCardDef(
    guid="8ee9e2f6-2010-5cd1-b830-f9721f632b60",
    key="NEO4",
    name="Miracle Energy",
    display_name="Miracle Energy",
    searchable_by=["Miracle Energy", "Special"],
    subtypes=["Special"],
    collector_number=16,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_TWO_AT_A_TIME,
    attach_to=attach_to_shining_or_light,
    discard_unless_attach_to=True,
    granted_abilities=[
        Ability(
            title="Miracle Energy",
            game_text="At the end of your turn, discard Miracle Energy.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=discard_energy_end_of_turn("8ee9e2f6-2010-5cd1-b830-f9721f632b60"),
        ),
    ],
)
