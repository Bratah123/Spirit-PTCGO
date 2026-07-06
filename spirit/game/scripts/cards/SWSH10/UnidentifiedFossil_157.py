from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b789c95c-2960-5f2c-ad54-88f7042fc565",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name",
    display_name="Unidentified Fossil",
    searchable_by=["Unidentified Fossil", "Item"],
    subtypes=["Item"],
    collector_number=157,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
