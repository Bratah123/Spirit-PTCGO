"""STUB: effect not implemented — do not guess mechanics.
Stark Mountain (DP6 #135): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Once during each player's turn, that player may choose a Fire or Fighting Energy attached to 1 of his or her Pokémon and move that Energy to 1 of his or her Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="5a1c2410-eb89-569e-9709-ba7f582a1d06",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StarkMountain.Name",
    display_name="Stark Mountain",
    searchable_by=["Stark Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=135,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
