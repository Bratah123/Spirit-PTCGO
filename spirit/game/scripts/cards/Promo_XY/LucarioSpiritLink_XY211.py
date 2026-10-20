"""STUB: effect not implemented — do not guess mechanics.
Lucario Spirit Link (Promo_XY #XY211): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Lucario-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f898599a-60e0-536e-a55b-cd59b31e283f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LucarioSpiritLink.Name",
    display_name="Lucario Spirit Link",
    searchable_by=["Lucario Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=211,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
