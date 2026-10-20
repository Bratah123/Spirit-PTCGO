"""STUB: effect not implemented — do not guess mechanics.
All-Night Party (XY9 #96): trainer effect stubbed.

Card text:
  - Once during each player's turn, if that player's Active Pokémon is Asleep, he or she may remove that Special Condition and heal 30 damage from that Pokémon.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="06cda8ff-46cf-5b60-8302-9eab2e539f61",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AllNightParty.Name",
    display_name="All-Night Party",
    searchable_by=["All-Night Party", "Stadium"],
    subtypes=["Stadium"],
    collector_number=96,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
