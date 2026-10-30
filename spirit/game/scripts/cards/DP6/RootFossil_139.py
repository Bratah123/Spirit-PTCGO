"""STUB: effect not implemented — do not guess mechanics.
Root Fossil (DP6 #139): trainer effect stubbed.

Card text:
  - Play Root Fossil as if it were a Colorless Basic Pokémon. (Root Fossil counts as a Trainer card as well, but if Root Fossil is Knocked Out, this counts as a Knocked Out Pokémon.) Root Fossil can't be affected by any Special Conditions and can't retreat. At any time during your turn before your attack, you may discard Root Fossil from play. (This doesn't count as a Knocked Out Pokémon.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e9dfe1c6-e7aa-59f8-93ef-294edcc65065",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossil.Name",
    display_name="Root Fossil",
    searchable_by=["Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=139,
    set_code="DP6",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
