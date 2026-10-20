"""STUB: effect not implemented — do not guess mechanics.
Beedrill Spirit Link (Promo_XY #XY159): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Beedrill-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="2c1ddbf0-e0e9-5a3c-a071-52f5553dea7b",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeedrillSpiritLink.Name",
    display_name="Beedrill Spirit Link",
    searchable_by=["Beedrill Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=159,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
