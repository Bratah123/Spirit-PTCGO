"""STUB: effect not implemented — do not guess mechanics.
Conductive Quarry (DP7 #82): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Once during each player's turn, the player may flip a coin. If heads, that player searches his or her discard pile for a Lightning or Metal Energy card, shows it to the opponent, and puts it into his or her hand.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="3c15ea4d-c419-5041-a60d-a8a453342795",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ConductiveQuarry.Name",
    display_name="Conductive Quarry",
    searchable_by=["Conductive Quarry", "Stadium"],
    subtypes=["Stadium"],
    collector_number=82,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
