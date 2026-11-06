"""Herbal Energy (XY3 #103): scripted (spirit.game.card_effects.xy_energies).

Card text:
  - This card can only be attached to Grass Pokémon. This card provides Grass Energy only while this card is attached to a Grass Pokémon.
  - When you attach this card from your hand to 1 of your Grass Pokémon, heal 30 damage from that Pokémon.
  - (If this card is attached to anything other than a Grass Pokémon, discard this card.)
"""

from spirit.game.card_effects.xy_energies import only_type, herbal_on_attach
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="bfab5dfb-d17a-5dd9-86df-ab0632aebafe",
    key="XY3",
    name="Herbal Energy",
    display_name="Herbal Energy",
    searchable_by=["Herbal Energy", "Special"],
    subtypes=["Special"],
    collector_number=103,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=only_type(PokemonTypes.GRASS),
    provides=[[PokemonTypes.GRASS]],
    discard_unless_attach_to=True,
    on_attach=herbal_on_attach,
)
