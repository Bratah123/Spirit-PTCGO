"""STUB: effect not implemented — do not guess mechanics.
Training Center (XY3 #102): trainer effect stubbed.

Card text:
  - Each Stage 1 and Stage 2 Pokémon in play (both yours and your opponent's) gets +30 HP.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="9f716805-d6d8-5400-bd3a-d295e751aacd",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainingCenter.Name",
    display_name="Training Center",
    searchable_by=["Training Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=102,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
