"""STUB: effect not implemented — do not guess mechanics.
Old Amber (DP5 #84): trainer effect stubbed.

Card text:
  - Play Old Amber as if it were a Colorless Basic Pokémon. (Old Amber counts as a Trainer card as well, but if Old Amber is Knocked Out, this counts as a Knocked Out Pokémon.) Old Amber can't be affected by any Special Conditions and can't retreat. At any time during your turn before your attack, you may discard Old Amber from play. (This doesn't count as a Knocked Out Pokémon.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="03b1abf8-58fa-542e-8949-b41088965dd1",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldAmber.Name",
    display_name="Old Amber",
    searchable_by=["Old Amber", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
