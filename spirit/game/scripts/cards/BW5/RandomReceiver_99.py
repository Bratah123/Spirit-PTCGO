from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="055cc694-65da-5959-b0ea-53552a6d602c",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RandomReceiver.Name",
    display_name="Random Receiver",
    searchable_by=["Random Receiver", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
