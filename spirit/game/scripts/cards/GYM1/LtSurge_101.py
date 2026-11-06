from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import lt_surge, lt_surge_condition


card = ItemCardDef(
    guid="4af0f412-55ba-53d3-a3a5-ef0f37835c01",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurge.Name",
    display_name="Lt. Surge",
    searchable_by=["Lt. Surge"],
    subtypes=[],
    collector_number=101,
    set_code="GYM1",
    rarity=Rarities.Rare,
    condition=lt_surge_condition,
    effect=lt_surge,
)
