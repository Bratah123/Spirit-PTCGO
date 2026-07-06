from spirit.game.card_effects.trainers import kabu
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f91f6930-6e7f-5541-b5f7-d44206d37b9a",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kabu.Name",
    display_name="Kabu",
    searchable_by=["Kabu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="SWSH35",
    rarity=Rarities.RareRainbow,
    effect=kabu
)
