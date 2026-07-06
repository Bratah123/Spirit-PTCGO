from spirit.game.card_effects.trainers import zisu
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8deabaa7-ea95-5460-a352-ee611b5a2a5e",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zisu.Name",
    display_name="Zisu",
    searchable_by=["Zisu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=207,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=zisu
)
