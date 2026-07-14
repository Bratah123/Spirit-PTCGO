from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="963902d0-48a5-507a-ae11-816234a0cd76",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=141,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
