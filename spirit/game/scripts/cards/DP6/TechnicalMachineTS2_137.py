"""STUB: effect not implemented — do not guess mechanics.
Technical Machine TS-2 (DP6 #137): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon in play. That Pokémon may use this card's attack instead of its own.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="ddee6153-1201-58c8-a1ff-be620ae99d18",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineTS2.Name",
    display_name="Technical Machine TS-2",
    searchable_by=["Technical Machine TS-2", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=137,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
