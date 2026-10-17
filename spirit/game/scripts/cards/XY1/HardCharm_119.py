"""STUB: effect not implemented — do not guess mechanics.
Hard Charm (XY1 #119): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Any damage done to the Pokémon this card is attached to by an opponent's attack is reduced by 20 (after applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="19d26a1b-854f-50cb-a065-43287acb1299",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HardCharm.Name",
    display_name="Hard Charm",
    searchable_by=["Hard Charm", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=119,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
