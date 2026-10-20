"""STUB: effect not implemented — do not guess mechanics.
Max Elixir (XY9 #102): trainer effect stubbed.

Card text:
  - Look at the top 6 cards of your deck and attach a basic Energy card you find there to a Basic Pokémon on your Bench. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ca3e1f3e-07b4-572a-aa4d-707069c20eed",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxElixir.Name",
    display_name="Max Elixir",
    searchable_by=["Max Elixir", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
