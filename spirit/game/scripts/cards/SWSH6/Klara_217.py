from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import klara

card = SupporterCardDef(
    guid="fa417a1f-87bd-5997-aad1-a0a4adb79e8d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Klara.Name",
    display_name="Klara",
    searchable_by=["Klara", "Supporter"],
    subtypes=["Supporter"],
    collector_number=217,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    effect=klara
)
