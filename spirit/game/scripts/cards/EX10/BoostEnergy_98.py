"""STUB: effect not implemented — do not guess mechanics.
Boost Energy (EX10 #98): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Boost Energy can be attached only to an Evolved Pokémon. Discard Boost Energy at the end of the turn it was attached. Boost Energy provides ColorlessColorlessColorless Energy. The Pokémon Boost Energy is attached to can't retreat. If the Pokémon Boost Energy is attached to isn't an Evolved Pokémon, discard Boost Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a789f01f-a171-5d3e-a3c6-43a4649bdbb9",
    key="EX10",
    name="Boost Energy",
    display_name="Boost Energy",
    searchable_by=["Boost Energy", "Special"],
    subtypes=["Special"],
    collector_number=98,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
