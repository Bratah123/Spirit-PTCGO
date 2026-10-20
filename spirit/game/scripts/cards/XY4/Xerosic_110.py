"""STUB: effect not implemented — do not guess mechanics.
Xerosic (XY4 #110): trainer effect stubbed.

Card text:
  - Choose a Pokémon Tool or Special Energy card attached to a Pokémon in play (yours or your opponent's) and discard it.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="889f550f-ffa6-5873-9433-1cf8c8f15db5",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Xerosic.Name",
    display_name="Xerosic",
    searchable_by=["Xerosic", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
