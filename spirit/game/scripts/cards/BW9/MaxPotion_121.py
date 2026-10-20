from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="42205f50-1152-5e54-bffa-40dd6aba0712",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=121,
    set_code="BW9",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
