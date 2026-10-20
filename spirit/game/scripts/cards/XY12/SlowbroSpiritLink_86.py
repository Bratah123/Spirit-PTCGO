"""STUB: effect not implemented — do not guess mechanics.
Slowbro Spirit Link (XY12 #86): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Slowbro-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="13c4fa65-fa0a-5248-b9f3-1ed5851b8e63",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SlowbroSpiritLink.Name",
    display_name="Slowbro Spirit Link",
    searchable_by=["Slowbro Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=86,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
