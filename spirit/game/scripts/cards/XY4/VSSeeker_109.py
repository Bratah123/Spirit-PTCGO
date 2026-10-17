"""STUB: effect not implemented — do not guess mechanics.
VS Seeker (XY4 #109): trainer effect stubbed.

Card text:
  - Put a Supporter card from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f8bef826-caea-5575-926e-0ffca16f2c5e",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
