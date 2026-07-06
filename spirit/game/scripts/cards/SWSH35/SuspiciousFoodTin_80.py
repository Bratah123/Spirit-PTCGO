from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e308d253-7bdb-53bf-afd3-489be5af1e07",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuspiciousFoodTin.Name",
    display_name="Suspicious Food Tin",
    searchable_by=["Suspicious Food Tin", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="SWSH35",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
