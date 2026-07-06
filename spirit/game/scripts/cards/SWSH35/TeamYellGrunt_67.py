from spirit.game.card_effects.trainers import team_yell_grunt, opponent_has_energy_attached
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="460f3690-b0d7-5a1f-be06-62acf85020ba",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamYellGrunt.Name",
    display_name="Team Yell Grunt",
    searchable_by=["Team Yell Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=67,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=team_yell_grunt,
    condition=opponent_has_energy_attached
)
