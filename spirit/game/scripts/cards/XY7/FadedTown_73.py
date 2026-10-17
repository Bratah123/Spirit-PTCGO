"""STUB: effect not implemented — do not guess mechanics.
Faded Town (XY7 #73): trainer effect stubbed.

Card text:
  - At any time between turns, put 2 damage counters on each Mega Evolution Pokémon.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="7c3fbfb4-e8e8-5fba-aa41-921b5747b179",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FadedTown.Name",
    display_name="Faded Town",
    searchable_by=["Faded Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=73,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
