from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="61e3f292-cf28-5c6a-83a1-9649a3289c5b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=160,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
