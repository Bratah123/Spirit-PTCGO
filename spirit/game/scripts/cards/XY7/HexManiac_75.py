"""STUB: effect not implemented — do not guess mechanics.
Hex Maniac (XY7 #75): trainer effect stubbed.

Card text:
  - Until the end of your opponent's next turn, each Pokémon in play, in each player's hand, and in each player's discard pile has no Abilities. (This includes cards that come into play on that turn.)
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="20a7e210-a23e-591b-96d4-807b0e9c6c50",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HexManiac.Name",
    display_name="Hex Maniac",
    searchable_by=["Hex Maniac", "Supporter"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
