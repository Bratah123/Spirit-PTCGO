from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1d4be05e-9ad0-58b7-ad67-03f57b9be313",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
