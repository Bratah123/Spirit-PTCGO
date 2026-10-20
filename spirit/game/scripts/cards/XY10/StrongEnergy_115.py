"""Strong Energy (XY10 #115): scripted (spirit.game.card_effects.xy_energies).

Card text:
  - This card can only be attached to Fighting Pokémon. This card provides Fighting Energy only while this card is attached to a Fighting Pokémon.
  - The attacks of the Fighting Pokémon this card is attached to do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - (If this card is attached to anything other than a Fighting Pokémon, discard this card.)
"""

from spirit.game.card_effects.xy_energies import only_type, StrongEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e102d84e-7447-5283-b2b4-db32af71a0c1",
    key="XY10",
    name="Strong Energy",
    display_name="Strong Energy",
    searchable_by=["Strong Energy", "Special"],
    subtypes=["Special"],
    collector_number=115,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=only_type(PokemonTypes.FIGHTING),
    provides=[[PokemonTypes.FIGHTING]],
    discard_unless_attach_to=True,
    passive=StrongEnergyPassive(),
)
