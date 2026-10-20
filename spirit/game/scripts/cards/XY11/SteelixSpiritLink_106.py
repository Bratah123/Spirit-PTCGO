"""STUB: effect not implemented — do not guess mechanics.
Steelix Spirit Link (XY11 #106): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Steelix-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="41d2f013-7517-5d9d-919f-60b12a9c1f7b",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SteelixSpiritLink.Name",
    display_name="Steelix Spirit Link",
    searchable_by=["Steelix Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=106,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
