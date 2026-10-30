"""TeamMagmaConspirator_82 wired."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import team_conspirator

card = SupporterCardDef(
    guid="57e43eca-5888-5767-8c3f-692192d3b576",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaConspirator.Name",
    display_name="Team Magma Conspirator",
    searchable_by=["Team Magma Conspirator", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=team_conspirator("Team Magma")
)
