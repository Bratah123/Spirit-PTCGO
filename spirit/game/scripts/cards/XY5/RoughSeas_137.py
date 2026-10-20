"""STUB: effect not implemented — do not guess mechanics.
Rough Seas (XY5 #137): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may heal 30 damage from each of his or her Water Pokémon and Lightning Pokémon.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="c6fc8d01-d342-5e2a-891a-4fa09765b4c5",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoughSeas.Name",
    display_name="Rough Seas",
    searchable_by=["Rough Seas", "Stadium"],
    subtypes=["Stadium"],
    collector_number=137,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
