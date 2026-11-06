from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import time_capsule


card = ItemCardDef(
    guid="c0f99755-400f-5af7-b06f-e74de09c7a56",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimeCapsule.Name",
    display_name="Time Capsule",
    searchable_by=["Time Capsule"],
    subtypes=[],
    collector_number=90,
    set_code="NEO1",
    rarity=Rarities.Rare,
    effect=time_capsule,
)
