"""Team Galactic's Mars (DP3 #126)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import team_galactics_mars

card = SupporterCardDef(
    guid="3ebd3900-f6d2-51bb-a8ce-032dbdf3ffdb",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsMars.Name",
    display_name="Team Galactic's Mars",
    searchable_by=["Team Galactic's Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=team_galactics_mars(),
)
