"""STUB: effect not implemented — do not guess mechanics.
N (XY10 #105a): trainer effect stubbed.

Card text:
  - Each player shuffles his or her hand into his or her deck. Then, each player draws a card for each of his or her remaining Prize cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="571125f2-970b-5bd1-b4f8-9ddc357f7975",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
