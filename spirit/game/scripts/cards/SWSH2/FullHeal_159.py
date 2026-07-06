from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ae5dbb3f-2b7e-5ca0-9eae-d15cbce462bd",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=159,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
