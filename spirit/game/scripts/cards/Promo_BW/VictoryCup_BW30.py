from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="56e5538f-f57c-5e2e-9d4b-8de6204257ea",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryCup.Name",
    display_name="Victory Cup",
    searchable_by=["Victory Cup", "Item"],
    subtypes=["Item"],
    collector_number=30,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
