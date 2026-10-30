"""Potion Energy (BASE6 #101).

Card text:
  If you play this card from your hand, remove 1 damage counter from the
  Pokémon you attach it to, if it has any. Potion Energy provides Colorless
  energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.ecard import potion_energy_on_attach

card = EnergyCardDef(
    guid="d21cdcec-701a-5e06-b618-9e274b71ad4d",
    key="BASE6",
    name="Potion Energy",
    display_name="Potion Energy",
    searchable_by=["Potion Energy", "Special"],
    subtypes=["Special"],
    collector_number=101,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    on_attach=potion_energy_on_attach,
)
