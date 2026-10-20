"""STUB: effect not implemented — do not guess mechanics.
Puzzle of Time (XY9 #109): trainer effect stubbed.

Card text:
  - You may play 2 Puzzle of Time cards at once.
• If you played 1 card, look at the top 3 cards of your deck and put them back in any order.
• If you played 2 cards, put 2 cards from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="28440831-0696-58c2-acd5-1ba1ea9f1721",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PuzzleofTime.Name",
    display_name="Puzzle of Time",
    searchable_by=["Puzzle of Time", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
