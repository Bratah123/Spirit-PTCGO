"""STUB: effect not implemented — do not guess mechanics.
Pidgeot Spirit Link (XY12 #81): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Pidgeot-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="7e0a1b1a-42f3-51d5-990b-ca969f82c375",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PidgeotSpiritLink.Name",
    display_name="Pidgeot Spirit Link",
    searchable_by=["Pidgeot Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=81,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
