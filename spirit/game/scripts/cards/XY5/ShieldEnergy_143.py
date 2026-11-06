"""Shield Energy (XY5 #143): scripted (spirit.game.card_effects.xy_energies).

Card text:
  - This card can only be attached to Metal Pokémon. This card provides Metal Energy only while this card is attached to a Metal Pokémon.
  - The attacks of your opponent's Pokémon do 10 less damage to the Metal Pokémon this card is attached to (before applying Weakness and Resistance).
  - (If this card is attached to anything other than a Metal Pokémon, discard this card.)
"""

from spirit.game.card_effects.xy_energies import only_type, ShieldEnergyPassive
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="69def66f-8b0b-5255-84ac-334cde669a32",
    key="XY5",
    name="Shield Energy",
    display_name="Shield Energy",
    searchable_by=["Shield Energy", "Special"],
    subtypes=["Special"],
    collector_number=143,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=only_type(PokemonTypes.METAL),
    provides=[[PokemonTypes.METAL]],
    discard_unless_attach_to=True,
    passive=ShieldEnergyPassive(),
)
