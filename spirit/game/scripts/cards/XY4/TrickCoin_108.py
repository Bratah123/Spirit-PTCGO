"""STUB: effect not implemented — do not guess mechanics.
Trick Coin (XY4 #108): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Once during your turn, after you flip any coins for an attack of the Pokémon this card is attached to, you may ignore all effects of those coin flips and begin flipping those coins again. (You may only use effects that let you flip coins again, including effects from other cards, once during your turn.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="7e429de7-9066-542d-b839-6c7e4177b718",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrickCoin.Name",
    display_name="Trick Coin",
    searchable_by=["Trick Coin", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=108,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
