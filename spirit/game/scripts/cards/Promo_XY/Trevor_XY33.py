"""STUB: effect not implemented — do not guess mechanics.
Trevor (Promo_XY #XY33): trainer effect stubbed.

Card text:
  - Search your deck for a Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="215733d5-9be6-58bd-a058-252d1a91c14f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Trevor.Name",
    display_name="Trevor",
    searchable_by=["Trevor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=33,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
