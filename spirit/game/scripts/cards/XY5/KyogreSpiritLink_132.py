"""STUB: effect not implemented — do not guess mechanics.
Kyogre Spirit Link (XY5 #132): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes Primal Kyogre-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="35f2feb9-347d-5271-ae27-8a8b3586c8c5",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KyogreSpiritLink.Name",
    display_name="Kyogre Spirit Link",
    searchable_by=["Kyogre Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=132,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
