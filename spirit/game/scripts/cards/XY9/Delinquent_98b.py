"""STUB: effect not implemented — do not guess mechanics.
Delinquent (XY9 #98b): trainer effect stubbed.

Card text:
  - Discard any Stadium card in play. If you do, your opponent discards 3 cards from his or her hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5555d1d1-0a03-5414-9173-a4cd85caf68d",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Delinquent.Name",
    display_name="Delinquent",
    searchable_by=["Delinquent", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
