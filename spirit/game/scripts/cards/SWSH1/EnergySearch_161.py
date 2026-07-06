from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bba87321-426f-594d-8e1d-d9c98719f975",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
