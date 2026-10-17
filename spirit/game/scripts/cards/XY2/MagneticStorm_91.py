"""STUB: effect not implemented — do not guess mechanics.
Magnetic Storm (XY2 #91): trainer effect stubbed.

Card text:
  - Each Pokémon in play has no Resistance.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="9148c756-7b30-5ce2-ba36-3ffac496e77e",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MagneticStorm.Name",
    display_name="Magnetic Storm",
    searchable_by=["Magnetic Storm", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
