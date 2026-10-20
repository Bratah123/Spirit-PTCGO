"""STUB: effect not implemented — do not guess mechanics.
Pokémon Fan Club (XY2 #106): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 Basic Pokémon, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f24d926d-83b8-5432-9ddd-0eb92c281771",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonFanClub.Name",
    display_name="Pok\u00e9mon Fan Club",
    searchable_by=["Pokémon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=106,
    set_code="XY2",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
