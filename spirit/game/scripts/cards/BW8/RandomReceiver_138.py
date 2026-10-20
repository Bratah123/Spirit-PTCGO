from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ee8f1352-2792-5a04-902a-cefd6892fc1a",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RandomReceiver.Name",
    display_name="Random Receiver",
    searchable_by=["Random Receiver", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="BW8",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
