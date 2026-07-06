from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="be893da7-2edb-575b-9220-f38f3f685444",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareFossil.Name",
    display_name="Rare Fossil",
    searchable_by=["Rare Fossil", "Item"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
