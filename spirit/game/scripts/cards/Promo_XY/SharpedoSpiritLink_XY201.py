"""STUB: effect not implemented — do not guess mechanics.
Sharpedo Spirit Link (Promo_XY #XY201): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Sharpedo-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="24a7f124-7f18-5fa3-ae7d-b9066c01728e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SharpedoSpiritLink.Name",
    display_name="Sharpedo Spirit Link",
    searchable_by=["Sharpedo Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=201,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
