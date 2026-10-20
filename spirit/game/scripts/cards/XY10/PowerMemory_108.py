"""STUB: effect not implemented — do not guess mechanics.
Power Memory (XY10 #108): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Zygarde-EX this card is attached to can also use the attack on this card. (You still need the necessary Energy to use this attack.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="3ea92e06-a056-54ae-a05d-99ccf7955aba",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerMemory.Name",
    display_name="Power Memory",
    searchable_by=["Power Memory", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=108,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
