"""STUB: effect not implemented — do not guess mechanics.
Snowpoint Temple (DP6 #134): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each Pokémon that isn't an Evolved Pokémon in play (both yours and your opponent's) gets +20 HP.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f349fdc6-52b6-50d8-a701-0234e66b83f0",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SnowpointTemple.Name",
    display_name="Snowpoint Temple",
    searchable_by=["Snowpoint Temple", "Stadium"],
    subtypes=["Stadium"],
    collector_number=134,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
