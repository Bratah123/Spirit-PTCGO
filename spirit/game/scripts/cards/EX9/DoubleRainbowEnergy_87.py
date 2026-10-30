"""STUB: effect not implemented — do not guess mechanics.
Double Rainbow Energy (EX9 #87): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Double Rainbow Energy can be attached only to an Evolved Pokémon (excluding Pokémon-ex). While in play, Double Rainbow Energy provides every type of Energy but provides 2 Energy at a time. (Has no effect other than providing Energy.) Damage done to your opponent's Pokémon by the Pokémon Double Rainbow Energy is attached to is reduced by 10 (before applying Weakness and Resistance). When the Pokémon Double Rainbow Energy is attached to is no longer an Evolved Pokémon, discard Double Rainbow Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="0d62d22f-8e27-53d8-8db0-4af214e10eed",
    key="EX9",
    name="Double Rainbow Energy",
    display_name="Double Rainbow Energy",
    searchable_by=["Double Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=87,
    set_code="EX9",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
