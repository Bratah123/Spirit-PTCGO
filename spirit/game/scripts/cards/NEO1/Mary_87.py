from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import mary, mary_playable


card = ItemCardDef(
    guid="0c3ceeb5-261d-59f2-b81a-a9ba9351e29d",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mary.Name",
    display_name="Mary",
    searchable_by=["Mary"],
    subtypes=[],
    collector_number=87,
    set_code="NEO1",
    rarity=Rarities.Rare,
    condition=mary_playable,
    effect=mary,
)
