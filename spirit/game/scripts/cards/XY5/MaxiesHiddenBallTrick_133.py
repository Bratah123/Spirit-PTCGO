"""STUB: effect not implemented — do not guess mechanics.
Maxie's Hidden Ball Trick (XY5 #133): trainer effect stubbed.

Card text:
  - You can play this card only when it is the last card in your hand.
  - Put a Fighting Pokémon from your discard pile onto your Bench. Then, draw 5 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="efa04d27-1a71-5a98-a0d9-d7a99c2c6795",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxiesHiddenBallTrick.Name",
    display_name="Maxie's Hidden Ball Trick",
    searchable_by=["Maxie's Hidden Ball Trick", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
