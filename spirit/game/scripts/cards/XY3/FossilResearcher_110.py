"""STUB: effect not implemented — do not guess mechanics.
Fossil Researcher (XY3 #110): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 in any combination of Amaura or Tyrunt and put them onto your bench. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c51e44de-fa49-56c8-a267-cad4ceeb693a",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilResearcher.Name",
    display_name="Fossil Researcher",
    searchable_by=["Fossil Researcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
