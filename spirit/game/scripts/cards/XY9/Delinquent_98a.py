"""STUB: effect not implemented — do not guess mechanics.
Delinquent (XY9 #98a): trainer effect stubbed.

Card text:
  - Discard any Stadium card in play. If you do, your opponent discards 3 cards from his or her hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f9cc2c7e-cb58-54fd-a6e3-d925953137fb",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Delinquent.Name",
    display_name="Delinquent",
    searchable_by=["Delinquent", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
