"""STUB: effect not implemented — do not guess mechanics.
Ampharos Spirit Link (XY7 #70): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Ampharos-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="5d2a67b8-622d-59ef-96e3-98568fd23577",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmpharosSpiritLink.Name",
    display_name="Ampharos Spirit Link",
    searchable_by=["Ampharos Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=70,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
