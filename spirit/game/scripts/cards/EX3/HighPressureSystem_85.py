from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import high_pressure_passive

card = StadiumCardDef(
    guid="09d88e23-ac14-5d36-8758-156b04401644",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HighPressureSystem.Name",
    display_name="High Pressure System",
    searchable_by=["High Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=85,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    passive=high_pressure_passive(),
)
