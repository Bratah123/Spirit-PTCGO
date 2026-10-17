"""STUB: effect not implemented — do not guess mechanics.
Latios Spirit Link (XY6 #85): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Latios-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="75dab4eb-d11f-50a6-b054-0086c77f4437",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LatiosSpiritLink.Name",
    display_name="Latios Spirit Link",
    searchable_by=["Latios Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=85,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
