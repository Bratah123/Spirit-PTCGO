"""STUB: effect not implemented — do not guess mechanics.
VS Seeker (XY6 #110): trainer effect stubbed.

Card text:
  - Put a Supporter card from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f499207a-db1a-5bdd-a33c-776871533a3f",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=110,
    set_code="XY6",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
