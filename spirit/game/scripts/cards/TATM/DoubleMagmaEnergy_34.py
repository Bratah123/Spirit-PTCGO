"""Double Magma Energy (TATM #34): scripted (spirit.game.card_effects.xy_energies).

Card text:
  - This card can only be attached to Team Magma Pokémon. Discard this card at the end of the turn you attached it.
  - This card provides FightingFighting Energy only while it is attached to a Team Magma Pokémon.
  - (If this card is attached to anything other than a Team Magma Pokémon, discard this card.)
"""

from spirit.game.card_effects.xy_energies import only_named
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="cf3d6a67-253e-5727-b284-ce8ba6540fb8",
    key="TATM",
    name="Double Magma Energy",
    display_name="Double Magma Energy",
    searchable_by=["Double Magma Energy", "Special"],
    subtypes=["Special"],
    collector_number=34,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=only_named("Team Magma's"),
    provides=[[PokemonTypes.FIGHTING, PokemonTypes.FIGHTING]],
    discard_unless_attach_to=True,
    discard_end_of_attach_turn=True,
)
