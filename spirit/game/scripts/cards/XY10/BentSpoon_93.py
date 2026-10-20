"""STUB: effect not implemented — do not guess mechanics.
Bent Spoon (XY10 #93): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all effects of your opponent's attacks, except damage, done to the Pokémon this card is attached to. (Existing effects are not removed.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="ca356f20-8348-56dc-8aa3-f650d36c0f43",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BentSpoon.Name",
    display_name="Bent Spoon",
    searchable_by=["Bent Spoon", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=93,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
