"""TeamAquaHideout_78 wired."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import team_hideout_retreat_passive

card = StadiumCardDef(
    guid="0a0b1ff6-c5b0-5cee-b5a1-f2a785a8a4da",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaHideout.Name",
    display_name="Team Aqua Hideout",
    searchable_by=["Team Aqua Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=78,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    passive=team_hideout_retreat_passive("Team Aqua")
)
