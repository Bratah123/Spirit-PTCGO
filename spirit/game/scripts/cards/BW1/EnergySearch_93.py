from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="afcd74ce-1221-5b41-97be-d243d8d2f542",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="BW1",
    rarity=Rarities.Common,
    effect=unimplemented
)
