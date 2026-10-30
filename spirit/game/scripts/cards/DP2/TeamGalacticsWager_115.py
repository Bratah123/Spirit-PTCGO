"""Team Galactic's Wager (DP2 #115)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import team_galactics_wager

card = SupporterCardDef(
    guid="0f31d040-2705-5e38-86cf-53e7669a73a8",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsWager.Name",
    display_name="Team Galactic's Wager",
    searchable_by=["Team Galactic's Wager", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=team_galactics_wager(),
)
