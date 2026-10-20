"""STUB: effect not implemented — do not guess mechanics.
Imakuni? (TwentiethAnn #63): trainer effect stubbed.

Card text:
  - Your Active Pokémon is now Confused.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="341cc365-8750-5f9e-b179-09265beb7dac",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Imakuni.Name",
    display_name="Imakuni?",
    searchable_by=["Imakuni?", "Supporter"],
    subtypes=["Supporter"],
    collector_number=63,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
