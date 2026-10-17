"""STUB: effect not implemented — do not guess mechanics.
Ace Trainer (XY7 #69): trainer effect stubbed.

Card text:
  - You can play this card only if you have more Prize cards left than your opponent.
  - Each player shuffles his or her hand into his or her deck. Then, draw 6 cards. Your opponent draws 3 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a1cdecf5-5c0e-5f3c-bf0f-16e31db744d8",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AceTrainer.Name",
    display_name="Ace Trainer",
    searchable_by=["Ace Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
