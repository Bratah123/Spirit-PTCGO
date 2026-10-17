"""STUB: effect not implemented — do not guess mechanics.
Sceptile Spirit Link (XY7 #80): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Sceptile-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="10fcc41f-db20-5a45-8a20-c144cb23836a",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SceptileSpiritLink.Name",
    display_name="Sceptile Spirit Link",
    searchable_by=["Sceptile Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=80,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
