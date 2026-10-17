"""STUB: effect not implemented — do not guess mechanics.
Fairy Garden (XY1 #117): trainer effect stubbed.

Card text:
  - Each Pokémon that has any Fairy Energy attached to it (both yours and your opponent's) has no Retreat Cost.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="3795d02e-1bd6-5a7f-8d79-c1b2548cd42d",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyGarden.Name",
    display_name="Fairy Garden",
    searchable_by=["Fairy Garden", "Stadium"],
    subtypes=["Stadium"],
    collector_number=117,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
