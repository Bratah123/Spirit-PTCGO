from spirit.game.card_effects.trainers import marnie
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ed3f56a6-383b-516b-a693-6f903d6b679f",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Marnie.Name",
    display_name="Marnie",
    searchable_by=["Marnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    effect=marnie
)
