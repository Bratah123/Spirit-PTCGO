"""STUB: effect not implemented — do not guess mechanics.
Brigette (XY8 #134): trainer effect stubbed.

Card text:
  - Search your deck for 1 Basic Pokémon-EX or 3 Basic Pokémon (except for Pokémon-EX) and put them onto your Bench. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="562e45e6-0f03-5a12-b9b3-9be90088ecb3",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brigette.Name",
    display_name="Brigette",
    searchable_by=["Brigette", "Supporter"],
    subtypes=["Supporter"],
    collector_number=134,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
