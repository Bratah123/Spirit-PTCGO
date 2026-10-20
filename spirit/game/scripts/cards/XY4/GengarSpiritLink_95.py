"""STUB: effect not implemented — do not guess mechanics.
Gengar Spirit Link (XY4 #95): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Gengar-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="d58378e9-5177-5aa3-8e33-3e99bb9a29ae",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GengarSpiritLink.Name",
    display_name="Gengar Spirit Link",
    searchable_by=["Gengar Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=95,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
