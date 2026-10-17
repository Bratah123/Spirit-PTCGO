"""STUB: effect not implemented — do not guess mechanics.
Wide Lens (XY6 #95): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Damage from the attacks of the Pokémon this card is attached to is affected by Weakness and Resistance for your opponent's Benched Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="3fc2f08d-eca4-5445-917f-671123b7bfda",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WideLens.Name",
    display_name="Wide Lens",
    searchable_by=["Wide Lens", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=95,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
