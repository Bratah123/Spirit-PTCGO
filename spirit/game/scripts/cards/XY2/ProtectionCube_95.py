"""STUB: effect not implemented — do not guess mechanics.
Protection Cube (XY2 #95): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all damage done to the Pokémon this card is attached to by attacks it uses.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="460abd81-5454-5c75-9c5b-c6e4abc88cf3",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProtectionCube.Name",
    display_name="Protection Cube",
    searchable_by=["Protection Cube", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=95,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
