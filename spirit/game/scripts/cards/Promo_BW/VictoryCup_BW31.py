from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cca8d164-4e24-5053-bd85-d712ecf4d3cb",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryCup.Name",
    display_name="Victory Cup",
    searchable_by=["Victory Cup", "Item"],
    subtypes=["Item"],
    collector_number=31,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
