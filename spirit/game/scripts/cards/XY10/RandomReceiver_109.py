"""STUB: effect not implemented — do not guess mechanics.
Random Receiver (XY10 #109): trainer effect stubbed.

Card text:
  - Reveal cards from the top of your deck until you reveal a Supporter card. Put it into your hand. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="86e2527a-3144-5882-8aeb-902e28be98c8",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RandomReceiver.Name",
    display_name="Random Receiver",
    searchable_by=["Random Receiver", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
