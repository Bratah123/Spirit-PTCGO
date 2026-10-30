"""TeamMagmaSchemer_70 wired."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import team_schemer

card = SupporterCardDef(
    guid="7afae935-e342-5191-80bf-91948c09f657",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaSchemer.Name",
    display_name="Team Magma Schemer",
    searchable_by=["Team Magma Schemer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=70,
    set_code="EX4",
    rarity=Rarities.Common,
    effect=team_schemer("Team Magma")
)
