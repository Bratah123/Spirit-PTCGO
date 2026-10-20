"""STUB: effect not implemented — do not guess mechanics.
Gym Badge (Promo_XY #XY210): trainer effect stubbed.

Card text:
  - Flip a coin until you get tails. For each heads, draw a card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8ddb2aca-6bb0-55d5-ad75-b20d266a0f2a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GymBadge.Name",
    display_name="Gym Badge",
    searchable_by=["Gym Badge", "Item"],
    subtypes=["Item"],
    collector_number=210,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
