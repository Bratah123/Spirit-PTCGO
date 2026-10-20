"""STUB: effect not implemented — do not guess mechanics.
Greedy Dice (XY11 #102): trainer effect stubbed.

Card text:
  - You can play this card only if you took it as a face-down Prize card, before you put it into your hand.
  - Flip a coin. If heads, take 1 more Prize card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="648dacce-e658-5a62-8070-3236c9551900",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreedyDice.Name",
    display_name="Greedy Dice",
    searchable_by=["Greedy Dice", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
