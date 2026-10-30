"""STUB: effect not implemented — do not guess mechanics.
Dome Fossil (DP5 #89): trainer effect stubbed.

Card text:
  - Play Dome Fossil as if it were a Colorless Basic Pokémon. (Dome Fossil counts as a Trainer card as well, but if Dome Fossil is Knocked Out, this counts as a Knocked Out Pokémon.) Dome Fossil can't be affected by any Special Conditions and can't retreat. At any time during your turn before your attack, you may discard Dome Fossil from play. (This doesn't count as a Knocked Out Pokémon.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e0327650-e169-57b9-abdb-fbf3e5a73c32",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DomeFossil.Name",
    display_name="Dome Fossil",
    searchable_by=["Dome Fossil", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="DP5",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
