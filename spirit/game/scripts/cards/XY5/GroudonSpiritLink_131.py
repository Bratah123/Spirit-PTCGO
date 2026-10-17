"""STUB: effect not implemented — do not guess mechanics.
Groudon Spirit Link (XY5 #131): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes Primal Groudon-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="0184f277-0cee-5608-ac16-3e719b735552",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GroudonSpiritLink.Name",
    display_name="Groudon Spirit Link",
    searchable_by=["Groudon Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=131,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
