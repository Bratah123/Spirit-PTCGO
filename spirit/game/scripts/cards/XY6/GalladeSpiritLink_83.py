"""STUB: effect not implemented — do not guess mechanics.
Gallade Spirit Link (XY6 #83): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Gallade-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="2a8eddad-33cc-53b3-adbc-b1517bece3c3",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GalladeSpiritLink.Name",
    display_name="Gallade Spirit Link",
    searchable_by=["Gallade Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=83,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
