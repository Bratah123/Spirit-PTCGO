"""STUB: effect not implemented — do not guess mechanics.
Rayquaza Spirit Link (XY6 #87): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Rayquaza-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="1c0005d5-edf2-56fa-a770-e002b2687554",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RayquazaSpiritLink.Name",
    display_name="Rayquaza Spirit Link",
    searchable_by=["Rayquaza Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=87,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
