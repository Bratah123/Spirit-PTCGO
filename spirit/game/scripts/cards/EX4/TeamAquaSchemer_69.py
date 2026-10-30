"""TeamAquaSchemer_69 wired."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import team_schemer

card = SupporterCardDef(
    guid="755aee45-0ba8-5bab-bc47-f3faf4638fec",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaSchemer.Name",
    display_name="Team Aqua Schemer",
    searchable_by=["Team Aqua Schemer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="EX4",
    rarity=Rarities.Common,
    effect=team_schemer("Team Aqua")
)
