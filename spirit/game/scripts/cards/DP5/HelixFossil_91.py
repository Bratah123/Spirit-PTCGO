"""STUB: effect not implemented — do not guess mechanics.
Helix Fossil (DP5 #91): trainer effect stubbed.

Card text:
  - Play Helix Fossil as if it were a Colorless Basic Pokémon. (Helix Fossil counts as a Trainer card as well, but if Helix Fossil is Knocked Out, this counts as a Knocked Out Pokémon.) Helix Fossil can't be affected by any Special Conditions and can't retreat. At any time during your turn before your attack, you may discard Helix Fossil from play. (This doesn't count as a Knocked Out Pokémon.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c1049325-3e43-5e19-bd5f-fb1ee21324be",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HelixFossil.Name",
    display_name="Helix Fossil",
    searchable_by=["Helix Fossil", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="DP5",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
