from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1b3890d6-4786-5fe6-aa3e-8afc54ada2e2",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaBall.Name",
    display_name="Team Plasma Ball",
    searchable_by=["Team Plasma Ball", "Item", "Team Plasma"],
    subtypes=["Item", "Team Plasma"],
    collector_number=105,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
