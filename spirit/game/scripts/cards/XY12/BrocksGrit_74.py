"""STUB: effect not implemented — do not guess mechanics.
Brock's Grit (XY12 #74): trainer effect stubbed.

Card text:
  - Shuffle 6 in any combination of Pokémon and basic Energy cards from your discard pile into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="84280e62-8e67-5282-b954-38cc270be2f4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=74,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
