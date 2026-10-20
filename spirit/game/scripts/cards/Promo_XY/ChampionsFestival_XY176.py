"""STUB: effect not implemented — do not guess mechanics.
Champions Festival (Promo_XY #XY176): trainer effect stubbed.

Card text:
  - Once during each player's turn, if that player has 6 Pokémon in play, he or she may heal 10 damage from each of his or her Pokémon.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="9bcd0311-7133-5c36-b213-f77c64312bb9",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=176,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
