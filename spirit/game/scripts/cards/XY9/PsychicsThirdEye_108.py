"""STUB: effect not implemented — do not guess mechanics.
Psychic's Third Eye (XY9 #108): trainer effect stubbed.

Card text:
  - Your opponent reveals his or her hand.
  - Discard as many cards as you like from your hand. Then, draw that many cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c0c48f4f-0d69-5b91-af3f-1f25caf3e771",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicsThirdEye.Name",
    display_name="Psychic's Third Eye",
    searchable_by=["Psychic's Third Eye", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
