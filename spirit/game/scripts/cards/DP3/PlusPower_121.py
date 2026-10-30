"""STUB: effect not implemented — do not guess mechanics.
PlusPower (DP3 #121): trainer effect stubbed.

Card text:
  - Attach PlusPower to 1 of your Pokémon. Discard this card at the end of your turn.
  - If the Pokémon PlusPower is attached to attacks, the attack does 10 more damage to the Active Pokémon (before applying Weakness and Resistance).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="94526f6a-cfa6-5dec-9819-2798ae52e5c8",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=121,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
