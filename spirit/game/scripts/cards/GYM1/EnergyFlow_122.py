from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import energy_flow, energy_flow_condition


card = ItemCardDef(
    guid="9f399bfb-7cd0-5012-9ab0-577c3ad61020",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyFlow.Name",
    display_name="Energy Flow",
    searchable_by=["Energy Flow"],
    subtypes=[],
    collector_number=122,
    set_code="GYM1",
    rarity=Rarities.Common,
    condition=energy_flow_condition,
    effect=energy_flow,
)
