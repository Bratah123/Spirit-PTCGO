from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import low_pressure_passive

card = StadiumCardDef(
    guid="f6ed8a60-ba95-5aeb-bac2-ee619b612f81",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LowPressureSystem.Name",
    display_name="Low Pressure System",
    searchable_by=["Low Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=86,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    passive=low_pressure_passive(10),
)
