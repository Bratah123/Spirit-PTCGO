"""TeamMagmaBall_80 wired."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import team_ball

card = ItemCardDef(
    guid="918dc69a-2573-5528-a2c9-c892c386e373",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaBall.Name",
    display_name="Team Magma Ball",
    searchable_by=["Team Magma Ball", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=team_ball("Team Magma")
)
