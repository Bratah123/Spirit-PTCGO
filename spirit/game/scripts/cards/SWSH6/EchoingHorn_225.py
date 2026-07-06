from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0f436eba-266c-5569-9f0e-7bbf3e369626",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EchoingHorn.Name",
    display_name="Echoing Horn",
    searchable_by=["Echoing Horn", "Item", "Rapid Strike"],
    subtypes=["Item", "Rapid Strike"],
    collector_number=225,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
