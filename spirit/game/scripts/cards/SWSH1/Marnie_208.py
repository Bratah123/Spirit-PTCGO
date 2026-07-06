from spirit.game.card_effects.trainers import marnie
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="81b2f2ca-b011-59ff-83b3-5110b8d37780",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Marnie.Name",
    display_name="Marnie",
    searchable_by=["Marnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="SWSH1",
    rarity=Rarities.RareRainbow,
    effect=marnie
)
