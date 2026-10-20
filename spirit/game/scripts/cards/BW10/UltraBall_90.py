from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8a54334f-2780-514e-b8fd-bc3e4391839a",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
