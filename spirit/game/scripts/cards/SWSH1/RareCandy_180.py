from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="deada367-2b30-5ab0-a4f8-2183298fd72b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=180,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
