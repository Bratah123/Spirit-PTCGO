from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import minion_of_team_rocket


card = ItemCardDef(
    guid="b8630af1-bc33-5a85-b609-2ce96111429d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MinionofTeamRocket.Name",
    display_name="Minion of Team Rocket",
    searchable_by=["Minion of Team Rocket"],
    subtypes=[],
    collector_number=113,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=minion_of_team_rocket,
)
