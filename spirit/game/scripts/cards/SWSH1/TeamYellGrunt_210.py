from spirit.game.card_effects.trainers import team_yell_grunt, opponent_has_energy_attached
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6feb9114-db1c-5347-90d8-c7cedaaa2314",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamYellGrunt.Name",
    display_name="Team Yell Grunt",
    searchable_by=["Team Yell Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=210,
    set_code="SWSH1",
    rarity=Rarities.RareRainbow,
    effect=team_yell_grunt,
    condition=opponent_has_energy_attached
)
