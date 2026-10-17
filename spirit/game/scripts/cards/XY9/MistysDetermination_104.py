"""STUB: effect not implemented — do not guess mechanics.
Misty's Determination (XY9 #104): trainer effect stubbed.

Card text:
  - Discard a card from your hand. If you do, look at the top 8 cards of your deck and put 1 of them into your hand. Shuffle the other cards back into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="06ef6071-19b1-5271-bd2f-75c68a9a5529",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDetermination.Name",
    display_name="Misty's Determination",
    searchable_by=["Misty's Determination", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
