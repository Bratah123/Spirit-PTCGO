"""STUB: effect not implemented — do not guess mechanics.
Korrina (XY3 #95): trainer effect stubbed.

Card text:
  - Search your deck for a Fighting Pokémon and an Item card, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="50075202-c637-561a-8e05-fa7a17ddf93f",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Korrina.Name",
    display_name="Korrina",
    searchable_by=["Korrina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
