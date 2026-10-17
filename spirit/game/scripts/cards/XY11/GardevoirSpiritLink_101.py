"""STUB: effect not implemented — do not guess mechanics.
Gardevoir Spirit Link (XY11 #101): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Gardevoir-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="b30be1a7-7788-52fd-bfc2-b5d272fac7ad",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GardevoirSpiritLink.Name",
    display_name="Gardevoir Spirit Link",
    searchable_by=["Gardevoir Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=101,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
