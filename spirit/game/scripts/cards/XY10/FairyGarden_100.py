"""STUB: effect not implemented — do not guess mechanics.
Fairy Garden (XY10 #100): trainer effect stubbed.

Card text:
  - Each Pokémon that has any Fairy Energy attached to it (both yours and your opponent's) has no Retreat Cost.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="d8690750-dcb9-57ad-95fa-d13f254cef14",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyGarden.Name",
    display_name="Fairy Garden",
    searchable_by=["Fairy Garden", "Stadium"],
    subtypes=["Stadium"],
    collector_number=100,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
