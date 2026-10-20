"""STUB: effect not implemented — do not guess mechanics.
Clemont (TwentiethAnn #59): trainer effect stubbed.

Card text:
  - Search your deck for up to 4 Lightning Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4ea788ee-a424-53d9-99c6-b7709a2b0fa4",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clemont.Name",
    display_name="Clemont",
    searchable_by=["Clemont", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
