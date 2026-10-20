"""STUB: effect not implemented — do not guess mechanics.
Altaria Spirit Link (XY10 #91): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Altaria-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="dfdaaf6f-f76d-50d3-9cb5-f96775892a35",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AltariaSpiritLink.Name",
    display_name="Altaria Spirit Link",
    searchable_by=["Altaria Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=91,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
