"""STUB: effect not implemented — do not guess mechanics.
Venusaur Spirit Link (XY12 #89): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Venusaur-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="df46868a-bfab-5571-afec-ddea0d59691e",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VenusaurSpiritLink.Name",
    display_name="Venusaur Spirit Link",
    searchable_by=["Venusaur Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=89,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
