"""STUB: effect not implemented — do not guess mechanics.
Aerodactyl Spirit Link (Promo_XY #XY99): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Aerodactyl-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="8abac291-21bd-5a5b-b36c-805cb16c68e6",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AerodactylSpiritLink.Name",
    display_name="Aerodactyl Spirit Link",
    searchable_by=["Aerodactyl Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
