"""LIGHT: real text lets Dark/Rocket's use gym attacks; approx -1 Colorless attack cost."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import rockets_tricky_gym_passive

card = StadiumCardDef(
    guid="38056161-8551-5f40-9ccc-966f315acdf6",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsTrickyGym.Name",
    display_name="Rocket's Tricky Gym",
    searchable_by=["Rocket's Tricky Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    passive=rockets_tricky_gym_passive(),
)
