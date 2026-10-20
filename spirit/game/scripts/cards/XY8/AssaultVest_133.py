"""STUB: effect not implemented — do not guess mechanics.
Assault Vest (XY8 #133): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Any damage done to the Pokémon this card is attached to by attacks from your opponent's Pokémon that have any Special Energy attached to them is reduced by 40 (after applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f54a3999-16b8-5b65-abd8-76ea5df7846f",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AssaultVest.Name",
    display_name="Assault Vest",
    searchable_by=["Assault Vest", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=133,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
