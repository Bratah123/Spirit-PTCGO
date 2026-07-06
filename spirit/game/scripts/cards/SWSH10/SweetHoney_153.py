from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d4fd0d96-df66-5e9d-ad5d-3cae2843aeaa",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SweetHoney.Name",
    display_name="Sweet Honey",
    searchable_by=["Sweet Honey", "Item"],
    subtypes=["Item"],
    collector_number=153,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
