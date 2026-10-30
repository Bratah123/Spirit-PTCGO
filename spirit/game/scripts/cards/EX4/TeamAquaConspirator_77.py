"""TeamAquaConspirator_77 wired."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import team_conspirator

card = SupporterCardDef(
    guid="5b9c5358-b321-50c1-81ce-e7b2dfac9360",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaConspirator.Name",
    display_name="Team Aqua Conspirator",
    searchable_by=["Team Aqua Conspirator", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=team_conspirator("Team Aqua")
)
