"""STUB: effect not implemented — do not guess mechanics.
Archie's Ace in the Hole (XY5 #157): trainer effect stubbed.

Card text:
  - You can play this card only when it is the last card in your hand.
  - Put a Water Pokémon from your discard pile onto your Bench. Then, draw 5 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e3b7848d-04cc-59df-a460-9f2d8f422c32",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArchiesAceintheHole.Name",
    display_name="Archie's Ace in the Hole",
    searchable_by=["Archie's Ace in the Hole", "Supporter"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
