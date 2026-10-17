"""STUB: effect not implemented — do not guess mechanics.
Manectric Spirit Link (XY4 #100): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Manectric-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="fa812de4-0871-5201-9b8e-53ea9e91f32a",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ManectricSpiritLink.Name",
    display_name="Manectric Spirit Link",
    searchable_by=["Manectric Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=100,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
