"""STUB: effect not implemented — do not guess mechanics.
Weakness Policy (XY5 #142): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Pokémon this card is attached to has no Weakness.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="28f11837-2e45-543d-8ec7-428ff0440a43",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WeaknessPolicy.Name",
    display_name="Weakness Policy",
    searchable_by=["Weakness Policy", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=142,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
