"""STUB: effect not implemented — do not guess mechanics.
Shadow Circle (XY1 #126): trainer effect stubbed.

Card text:
  - Each Pokémon that has any Darkness Energy attached to it (both yours and your opponent's) has no Weakness.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="afd45c1b-a248-5969-b353-fdc1f4061b38",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShadowCircle.Name",
    display_name="Shadow Circle",
    searchable_by=["Shadow Circle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=126,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
