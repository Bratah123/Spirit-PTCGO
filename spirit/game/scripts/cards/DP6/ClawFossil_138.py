"""STUB: effect not implemented — do not guess mechanics.
Claw Fossil (DP6 #138): trainer effect stubbed.

Card text:
  - Play Claw Fossil as if it were a Colorless Basic Pokémon. (Claw Fossil counts as a Trainer card as well, but if Claw Fossil is Knocked Out, this counts as a Knocked Out Pokémon.) Claw Fossil can't be affected by any Special Conditions and can't retreat. At any time during your turn before your attack, you may discard Claw Fossil from play. (This doesn't count as a Knocked Out Pokémon.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fb246ca9-8581-558e-81e2-ce65e6141c9d",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClawFossil.Name",
    display_name="Claw Fossil",
    searchable_by=["Claw Fossil", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="DP6",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
