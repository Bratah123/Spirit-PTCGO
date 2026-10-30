"""TeamAquaBall_75 wired."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import team_ball

card = ItemCardDef(
    guid="50e7f7f7-2dab-56b1-bd1a-aef5491f999a",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaBall.Name",
    display_name="Team Aqua Ball",
    searchable_by=["Team Aqua Ball", "Item"],
    subtypes=["Item"],
    collector_number=75,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=team_ball("Team Aqua")
)
