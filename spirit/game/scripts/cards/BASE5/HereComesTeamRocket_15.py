from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    here_comes_team_rocket,
    here_comes_team_rocket_condition,
)

card = ItemCardDef(
    guid="c1823d45-d150-54bc-ac26-4dcedad8870d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!"],
    subtypes=[],
    collector_number=15,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    effect=here_comes_team_rocket,
    condition=here_comes_team_rocket_condition,
)
