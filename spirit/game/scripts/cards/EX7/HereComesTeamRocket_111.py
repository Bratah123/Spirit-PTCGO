"""LIGHT: reveals Prize cards; persistent face-up for rest of game not fully tracked."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import here_comes_team_rocket

card = SupporterCardDef(
    guid="d8b31bbe-ade3-5ff4-a0b2-7f556a108a34",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="EX7",
    rarity=Rarities.RareSecret,
    effect=here_comes_team_rocket,
)
