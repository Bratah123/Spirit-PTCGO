"""STUB: effect not implemented — do not guess mechanics.
Aqua Diffuser (TATM #23): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Team Aqua Pokémon this card is attached to can also use the attack on this card. (You still need the necessary Energy to use this attack.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="c373ff38-28c1-5aee-9e52-dee864ade3ce",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AquaDiffuser.Name",
    display_name="Aqua Diffuser",
    searchable_by=["Aqua Diffuser", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=23,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
