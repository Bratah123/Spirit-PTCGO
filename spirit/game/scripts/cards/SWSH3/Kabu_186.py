from spirit.game.card_effects.trainers import kabu
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b6a93e85-813a-5de1-ad71-4326430eadc6",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kabu.Name",
    display_name="Kabu",
    searchable_by=["Kabu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    effect=kabu
)
