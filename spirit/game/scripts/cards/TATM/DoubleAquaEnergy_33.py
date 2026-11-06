"""Double Aqua Energy (TATM #33): scripted (spirit.game.card_effects.xy_energies).

Card text:
  - This card can only be attached to Team Aqua Pokémon. Discard this card at the end of the turn you attached it.
  - This card provides WaterWater Energy only while it is attached to a Team Aqua Pokémon.
  - (If this card is attached to anything other than a Team Aqua Pokémon, discard this card.)
"""

from spirit.game.card_effects.xy_energies import only_named
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="483ce702-6169-5dbe-9e8d-8f08a8a1bf52",
    key="TATM",
    name="Double Aqua Energy",
    display_name="Double Aqua Energy",
    searchable_by=["Double Aqua Energy", "Special"],
    subtypes=["Special"],
    collector_number=33,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=only_named("Team Aqua's"),
    provides=[[PokemonTypes.WATER, PokemonTypes.WATER]],
    discard_unless_attach_to=True,
    discard_end_of_attach_turn=True,
)
