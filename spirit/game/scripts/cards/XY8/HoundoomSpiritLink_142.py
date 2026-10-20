"""STUB: effect not implemented — do not guess mechanics.
Houndoom Spirit Link (XY8 #142): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Houndoom-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="31791748-c246-5d63-b8a0-595fde2b1f25",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HoundoomSpiritLink.Name",
    display_name="Houndoom Spirit Link",
    searchable_by=["Houndoom Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=142,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
