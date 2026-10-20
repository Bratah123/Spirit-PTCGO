"""STUB: effect not implemented — do not guess mechanics.
Brigette (XY8 #161): trainer effect stubbed.

Card text:
  - Search your deck for 1 Basic Pokémon-EX or 3 Basic Pokémon (except for Pokémon-EX), and put them onto your Bench. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a4b8533c-19cb-59b3-82f1-d18ad0243b96",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brigette.Name",
    display_name="Brigette",
    searchable_by=["Brigette", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
