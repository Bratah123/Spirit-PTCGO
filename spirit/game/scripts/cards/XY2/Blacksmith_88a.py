"""STUB: effect not implemented — do not guess mechanics.
Blacksmith (XY2 #88a): trainer effect stubbed.

Card text:
  - Attach 2 Fire Energy cards from your discard pile to 1 of your Fire Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="daa67b30-c096-5261-aa2b-dda00bfb0274",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blacksmith.Name",
    display_name="Blacksmith",
    searchable_by=["Blacksmith", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="XY2",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
