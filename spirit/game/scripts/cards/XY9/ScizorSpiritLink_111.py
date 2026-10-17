"""STUB: effect not implemented — do not guess mechanics.
Scizor Spirit Link (XY9 #111): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Scizor-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="18d0ecbd-9773-54b3-a02e-b41d581505ad",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScizorSpiritLink.Name",
    display_name="Scizor Spirit Link",
    searchable_by=["Scizor Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=111,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
