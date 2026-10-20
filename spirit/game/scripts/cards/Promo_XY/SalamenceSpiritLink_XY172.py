"""STUB: effect not implemented — do not guess mechanics.
Salamence Spirit Link (Promo_XY #XY172): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Salamence-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="94f2b74f-7dce-5534-b421-e611aa693cfb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SalamenceSpiritLink.Name",
    display_name="Salamence Spirit Link",
    searchable_by=["Salamence Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=172,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
