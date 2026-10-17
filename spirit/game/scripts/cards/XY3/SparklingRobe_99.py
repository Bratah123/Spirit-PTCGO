"""STUB: effect not implemented — do not guess mechanics.
Sparkling Robe (XY3 #99): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Pokémon this card is attached to can't be affected by any Special Conditions. (Remove any Special Conditions affecting that Pokémon.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f05087b3-ca20-5ec4-b850-b5db64d3d28b",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SparklingRobe.Name",
    display_name="Sparkling Robe",
    searchable_by=["Sparkling Robe", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=99,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
