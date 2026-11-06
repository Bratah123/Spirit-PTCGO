"""Dangerous Energy (XY7 #82): scripted (spirit.game.card_effects.xy_energies).

Card text:
  - This card can only be attached to Darkness Pokémon. This card provides Darkness Energy only while this card is attached to a Darkness Pokémon.
  - Whenever the Darkness Pokémon this card is attached to is your Active Pokémon and is damaged by an attack from your opponent's Pokémon-EX (even if that Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon-EX.
  - (If this card is attached to anything other than a Darkness Pokémon, discard this card.)
"""

from spirit.game.card_effects.xy_energies import only_type, dangerous_energy_damaged
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="78e5fa25-878f-55e7-bcd4-b3384e0143aa",
    key="XY7",
    name="Dangerous Energy",
    display_name="Dangerous Energy",
    searchable_by=["Dangerous Energy", "Special"],
    subtypes=["Special"],
    collector_number=82,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=only_type(PokemonTypes.DARKNESS),
    provides=[[PokemonTypes.DARKNESS]],
    discard_unless_attach_to=True,
    on_carrier_damaged_by_attack=dangerous_energy_damaged,
)
