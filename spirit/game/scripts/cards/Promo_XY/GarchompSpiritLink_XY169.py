"""STUB: effect not implemented — do not guess mechanics.
Garchomp Spirit Link (Promo_XY #XY169): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Garchomp-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="965ced53-6273-5689-96a0-b65727349df4",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GarchompSpiritLink.Name",
    display_name="Garchomp Spirit Link",
    searchable_by=["Garchomp Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=169,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
