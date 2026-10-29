"""STUB: playing 4 copies at once is not an engine action.
Missing Clover (SM5 #168): look at top (1 copy) / take a Prize (4 copies).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3fdc9e9b-1d3c-54a7-8dbf-0bc6e47e86ad",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MissingClover.Name",
    display_name="Missing Clover",
    searchable_by=["Missing Clover", "Item"],
    subtypes=["Item"],
    collector_number=168,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    # STUB: play-4-at-once Item mode is not supported
    effect=unimplemented
)
