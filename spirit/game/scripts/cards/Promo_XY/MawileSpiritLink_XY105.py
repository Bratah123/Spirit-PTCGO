"""STUB: effect not implemented — do not guess mechanics.
Mawile Spirit Link (Promo_XY #XY105): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Mawile-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="4f4c8a47-ce25-5e47-80b2-a0747557fe79",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MawileSpiritLink.Name",
    display_name="Mawile Spirit Link",
    searchable_by=["Mawile Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=105,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
