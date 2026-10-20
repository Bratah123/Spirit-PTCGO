"""STUB: effect not implemented — do not guess mechanics.
Karen (Promo_XY #XY177): trainer effect stubbed.

Card text:
  - Each player shuffles all Pokémon in his or her discard pile into his or her deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c84a5de9-5c43-5ec4-997e-5c6dfb670cf0",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Karen.Name",
    display_name="Karen",
    searchable_by=["Karen", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
