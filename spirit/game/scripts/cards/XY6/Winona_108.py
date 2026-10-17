"""STUB: effect not implemented — do not guess mechanics.
Winona (XY6 #108): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 Colorless Pokémon and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="df800b75-141c-52e4-bfb7-039b578a4057",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Winona.Name",
    display_name="Winona",
    searchable_by=["Winona", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="XY6",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
