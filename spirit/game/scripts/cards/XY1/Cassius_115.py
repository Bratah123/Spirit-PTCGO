"""STUB: effect not implemented — do not guess mechanics.
Cassius (XY1 #115): trainer effect stubbed.

Card text:
  - Shuffle 1 of your Pokémon and all cards attached to it into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9190592b-32c7-5093-9b78-20f93d475697",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cassius.Name",
    display_name="Cassius",
    searchable_by=["Cassius", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
