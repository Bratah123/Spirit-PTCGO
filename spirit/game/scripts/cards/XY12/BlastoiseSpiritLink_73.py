"""STUB: effect not implemented — do not guess mechanics.
Blastoise Spirit Link (XY12 #73): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Your turn does not end if the Pokémon this card is attached to becomes M Blastoise-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f2ed3342-ea03-5e98-954b-538ad8f79f09",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlastoiseSpiritLink.Name",
    display_name="Blastoise Spirit Link",
    searchable_by=["Blastoise Spirit Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=73,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
