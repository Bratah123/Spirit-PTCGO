from spirit.game.card_effects.trainers import piers
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="264b0f60-7330-52a5-8b40-be947d431e1d",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Piers.Name",
    display_name="Piers",
    searchable_by=["Piers", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="SWSH35",
    rarity=Rarities.RareRainbow,
    effect=piers
)
