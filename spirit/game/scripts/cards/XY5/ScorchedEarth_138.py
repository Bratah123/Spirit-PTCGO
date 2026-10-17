"""STUB: effect not implemented — do not guess mechanics.
Scorched Earth (XY5 #138): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may discard a Fire or Fighting Energy card from his or her hand. If that player does so, he or she draws 2 cards.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="1f4f46e7-f9fc-525e-978b-5934d5dab812",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScorchedEarth.Name",
    display_name="Scorched Earth",
    searchable_by=["Scorched Earth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=138,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
