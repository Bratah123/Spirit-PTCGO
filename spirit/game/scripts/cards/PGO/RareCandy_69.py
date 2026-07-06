from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="32e87eba-71ac-50f5-9e8e-46186f5d339b",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=69,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
