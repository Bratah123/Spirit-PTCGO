from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    here_comes_team_rocket,
    here_comes_team_rocket_condition,
)

card = ItemCardDef(
    guid="b4d76d4d-5509-55a2-a6d1-5dd01c53ec69",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!"],
    subtypes=[],
    collector_number=71,
    set_code="BASE5",
    rarity=Rarities.Rare,
    effect=here_comes_team_rocket,
    condition=here_comes_team_rocket_condition,
)
