"""STUB: playing 4 copies at once is not an engine action.
Missing Clover (SM5 #129): look at top (1 copy) / take a Prize (4 copies).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f4f75452-c5dd-52c5-bc11-0c8d9522f3bd",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MissingClover.Name",
    display_name="Missing Clover",
    searchable_by=["Missing Clover", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: play-4-at-once Item mode is not supported
    effect=unimplemented
)
