"""STUB: effect not implemented — do not guess mechanics.
Energy Link (DP7 #83): trainer effect stubbed.

Card text:
  - Attach Energy Link to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - As long as Energy Link is attached to a Pokémon, you may move an Energy card attached to that Pokémon to another of your Pokémon that has Energy Link attached to it. You may use this effect as often as you like during your turn.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="8c4b8026-7084-5f99-b6b7-6a54c876e7f5",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyLink.Name",
    display_name="Energy Link",
    searchable_by=["Energy Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=83,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
