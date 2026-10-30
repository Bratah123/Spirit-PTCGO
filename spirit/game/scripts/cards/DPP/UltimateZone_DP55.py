"""STUB: effect not implemented — do not guess mechanics.
Ultimate Zone (DPP #DP55): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - During each player's turn, the player may move an Energy card attached to 1 of his or her Benched Pokémon to his or her Active Arceus as often as he or she likes.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="05e5d4af-b11f-5bdf-8166-b427833da3e4",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltimateZone.Name",
    display_name="Ultimate Zone",
    searchable_by=["Ultimate Zone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=55,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
