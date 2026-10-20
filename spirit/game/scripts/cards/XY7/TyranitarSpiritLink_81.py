"""STUB: effect not implemented — do not guess mechanics.
Tyranitar Spirit Link (XY7 #81): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Tyranitar-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="ce1df9ad-1903-533a-b49d-895a74318263",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TyranitarSpiritLink.Name",
    display_name="Tyranitar Spirit Link",
    searchable_by=["Tyranitar Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=81,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
