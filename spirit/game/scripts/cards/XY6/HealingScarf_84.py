"""STUB: effect not implemented — do not guess mechanics.
Healing Scarf (XY6 #84): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Whenever you attach an Energy card from your hand to the Pokémon this card is attached to, heal 20 damage from it.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="3afe7f14-cec5-5487-b190-e53ffd5fbfa2",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingScarf.Name",
    display_name="Healing Scarf",
    searchable_by=["Healing Scarf", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=84,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
