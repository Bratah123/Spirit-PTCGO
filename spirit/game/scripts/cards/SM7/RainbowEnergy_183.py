"""Rainbow Energy (SM7 #183).

Card text:
  This card provides Colorless Energy.
  While in play, this card provides every type of Energy but provides only
  1 Energy at a time. When you attach this card from your hand to 1 of your
  Pokémon, put 1 damage counter on that Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    rainbow_energy_on_attach,
)

card = EnergyCardDef(
    guid="07c5bbba-ceb0-56de-8985-47d09aa100eb",
    key="SM7",
    name="Rainbow Energy",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=183,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    on_attach=rainbow_energy_on_attach,
)
