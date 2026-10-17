"""STUB: effect not implemented — do not guess mechanics.
Winona (XY6 #96): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 Colorless Pokémon and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2d508c1f-20bd-592d-a839-2043f63b4385",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Winona.Name",
    display_name="Winona",
    searchable_by=["Winona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
