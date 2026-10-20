"""STUB: effect not implemented — do not guess mechanics.
Bursting Balloon (XY9 #97): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn.
  - If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), put 6 damage counters on the Attacking Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="65745751-0123-5aa3-aec1-f443028b5b9f",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BurstingBalloon.Name",
    display_name="Bursting Balloon",
    searchable_by=["Bursting Balloon", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=97,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
