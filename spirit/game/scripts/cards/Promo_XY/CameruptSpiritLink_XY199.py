"""STUB: effect not implemented — do not guess mechanics.
Camerupt Spirit Link (Promo_XY #XY199): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Camerupt-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="cadfe4a4-853d-56c7-904c-2dd342b39545",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CameruptSpiritLink.Name",
    display_name="Camerupt Spirit Link",
    searchable_by=["Camerupt Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=199,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
