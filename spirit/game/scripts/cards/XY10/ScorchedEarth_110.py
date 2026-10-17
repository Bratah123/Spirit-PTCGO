"""STUB: effect not implemented — do not guess mechanics.
Scorched Earth (XY10 #110): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may discard a Fire or Fighting Energy card from his or her hand. If that player does so, he or she draws 2 cards.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f7889519-a4be-59dc-9f00-5dc4bfac83af",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScorchedEarth.Name",
    display_name="Scorched Earth",
    searchable_by=["Scorched Earth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=110,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
