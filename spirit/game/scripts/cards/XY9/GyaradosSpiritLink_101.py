"""STUB: effect not implemented — do not guess mechanics.
Gyarados Spirit Link (XY9 #101): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Gyarados-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="961fe2e5-7fe1-5bc4-9079-a98901a6ed54",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GyaradosSpiritLink.Name",
    display_name="Gyarados Spirit Link",
    searchable_by=["Gyarados Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=101,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
