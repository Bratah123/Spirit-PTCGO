from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import high_pressure_passive

card = StadiumCardDef(
    guid="22d23a20-bb72-53d7-8e09-a339d007e94c",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HighPressureSystem.Name",
    display_name="High Pressure System",
    searchable_by=["High Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=10,
    set_code="POP3",
    rarity=Rarities.Uncommon,
    passive=high_pressure_passive(),
)
