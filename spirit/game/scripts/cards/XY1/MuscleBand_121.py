"""STUB: effect not implemented — do not guess mechanics.
Muscle Band (XY1 #121): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The attacks of the Pokémon this card is attached to do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="80e07131-c5de-5aa2-9077-42d702d02f56",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MuscleBand.Name",
    display_name="Muscle Band",
    searchable_by=["Muscle Band", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=121,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
