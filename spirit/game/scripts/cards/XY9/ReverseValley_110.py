"""STUB: effect not implemented — do not guess mechanics.
Reverse Valley (XY9 #110): trainer effect stubbed.

Card text:
  - Choose which way this card faces before you play it. Any damage done to this ↓ player's Metal Pokémon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).
  - Choose which way this card faces before you play it. The attacks of this ↓ player's Darkness Pokémon do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="4243938d-79db-5a5e-889c-d38432a88f37",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReverseValley.Name",
    display_name="Reverse Valley",
    searchable_by=["Reverse Valley", "Stadium"],
    subtypes=["Stadium"],
    collector_number=110,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
