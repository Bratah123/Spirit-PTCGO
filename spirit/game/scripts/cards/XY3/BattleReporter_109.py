"""STUB: effect not implemented — do not guess mechanics.
Battle Reporter (XY3 #109): trainer effect stubbed.

Card text:
  - Draw cards until you have the same number of cards in your hand as your opponent.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c0b3a52a-81b9-55bf-bee9-03d6d5214416",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleReporter.Name",
    display_name="Battle Reporter",
    searchable_by=["Battle Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
