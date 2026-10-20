"""STUB: effect not implemented — do not guess mechanics.
Korrina (XY3 #111): trainer effect stubbed.

Card text:
  - Search your deck for a Fighting Pokémon and an Item card, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0a884062-fb4e-5970-ba25-7ae0834d6dd3",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Korrina.Name",
    display_name="Korrina",
    searchable_by=["Korrina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
