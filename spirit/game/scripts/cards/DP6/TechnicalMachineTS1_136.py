"""STUB: effect not implemented — do not guess mechanics.
Technical Machine TS-1 (DP6 #136): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon in play. That Pokémon may use this card's attack instead of its own.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="65de453d-0f58-56c9-8c0e-1c3996e89f3f",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineTS1.Name",
    display_name="Technical Machine TS-1",
    searchable_by=["Technical Machine TS-1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=136,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
