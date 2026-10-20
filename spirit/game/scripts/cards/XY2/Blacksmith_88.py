"""STUB: effect not implemented — do not guess mechanics.
Blacksmith (XY2 #88): trainer effect stubbed.

Card text:
  - Attach 2 Fire Energy cards from your discard pile to 1 of your Fire Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="bb354428-49ff-54d1-8b65-504d12c13bf0",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blacksmith.Name",
    display_name="Blacksmith",
    searchable_by=["Blacksmith", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
