"""STUB: effect not implemented — do not guess mechanics.
Heavy Boots (XY8 #141): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Retreat Cost of the Pokémon this card is attached to is 3 or more, that Pokémon gets +20 HP and can't be Confused. (If that Pokémon is currently Confused, remove that Special Condition.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="45cfde93-0bea-5428-b2b2-cc8af213e333",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBoots.Name",
    display_name="Heavy Boots",
    searchable_by=["Heavy Boots", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=141,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
