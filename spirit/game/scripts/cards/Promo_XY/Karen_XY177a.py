"""STUB: effect not implemented — do not guess mechanics.
Karen (Promo_XY #XY177a): trainer effect stubbed.

Card text:
  - Each player shuffles all Pokémon in his or her discard pile into his or her deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="cb26bdcb-9b05-54e7-bc13-06b12e1518e7",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Karen.Name",
    display_name="Karen",
    searchable_by=["Karen", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
