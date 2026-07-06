from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d17d2b10-6400-5d79-9ae6-63504e64447f",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureModule.Name",
    display_name="Lure Module",
    searchable_by=["Lure Module", "Item"],
    subtypes=["Item"],
    collector_number=67,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
