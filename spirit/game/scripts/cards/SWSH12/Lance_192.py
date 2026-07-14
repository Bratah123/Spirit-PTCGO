from spirit.game.card_effects.trainers import lance
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="99060318-68a6-5895-a0fe-f1ecd884cddc",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lance.Name",
    display_name="Lance",
    searchable_by=["Lance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=192,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    effect=lance
)
