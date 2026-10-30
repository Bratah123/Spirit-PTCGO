from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import lt_surge, lt_surge_condition


card = ItemCardDef(
    guid="fdfe2f97-6c95-5e31-a180-1d6b21f7f82a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurge.Name",
    display_name="Lt. Surge",
    searchable_by=["Lt. Surge"],
    subtypes=[],
    collector_number=17,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    condition=lt_surge_condition,
    effect=lt_surge,
)
