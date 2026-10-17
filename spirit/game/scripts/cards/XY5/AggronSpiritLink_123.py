"""STUB: effect not implemented — do not guess mechanics.
Aggron Spirit Link (XY5 #123): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Aggron-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f77d9ee0-9cce-5327-b761-1daf01b36b05",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AggronSpiritLink.Name",
    display_name="Aggron Spirit Link",
    searchable_by=["Aggron Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=123,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
