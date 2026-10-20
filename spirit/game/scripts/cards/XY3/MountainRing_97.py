"""STUB: effect not implemented — do not guess mechanics.
Mountain Ring (XY3 #97): trainer effect stubbed.

Card text:
  - Prevent all damage done to Benched Pokémon by attacks (both yours and your opponent's).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="c6c72ca5-6e31-5b00-a99d-cee00ca1c061",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MountainRing.Name",
    display_name="Mountain Ring",
    searchable_by=["Mountain Ring", "Stadium"],
    subtypes=["Stadium"],
    collector_number=97,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
