from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fa19c4be-76cf-5e0b-a6a4-571a70c6cf1b",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=104,
    set_code="BW1",
    rarity=Rarities.Common,
    effect=unimplemented
)
