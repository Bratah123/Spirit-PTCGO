from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import low_pressure_passive

card = StadiumCardDef(
    guid="7ad2a543-f166-5159-8471-289c581f147a",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LowPressureSystem.Name",
    display_name="Low Pressure System",
    searchable_by=["Low Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=11,
    set_code="POP3",
    rarity=Rarities.Uncommon,
    passive=low_pressure_passive(10),
)
