from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="15ba7894-6949-50f2-ae3f-976e87d8615f",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
