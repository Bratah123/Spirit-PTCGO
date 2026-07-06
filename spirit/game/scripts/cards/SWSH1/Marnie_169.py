from spirit.game.card_effects.trainers import marnie
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="28916b14-56ff-5306-9eb9-c7f5b44cfeba",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Marnie.Name",
    display_name="Marnie",
    searchable_by=["Marnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=169,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    effect=marnie
)
