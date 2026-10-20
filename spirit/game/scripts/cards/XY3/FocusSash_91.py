"""STUB: effect not implemented — do not guess mechanics.
Focus Sash (XY3 #91): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Fighting Pokémon this card is attached to has full HP and would be Knocked Out by damage from an opponent's attack, that Pokémon is not Knocked Out and its remaining HP becomes 10 instead. Then, discard this card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="aa83f6fc-449f-5100-9633-a1ff5d59271f",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FocusSash.Name",
    display_name="Focus Sash",
    searchable_by=["Focus Sash", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=91,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
