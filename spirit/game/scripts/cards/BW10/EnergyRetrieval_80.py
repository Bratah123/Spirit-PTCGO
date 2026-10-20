from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ce769df0-6b2b-52e1-8901-644c4c43d1e4",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
