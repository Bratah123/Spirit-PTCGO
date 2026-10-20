"""STUB: effect not implemented — do not guess mechanics.
Glalie Spirit Link (XY8 #139): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Glalie-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f14bf81b-b33b-5bbe-a0a6-a04e8032438c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlalieSpiritLink.Name",
    display_name="Glalie Spirit Link",
    searchable_by=["Glalie Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=139,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
