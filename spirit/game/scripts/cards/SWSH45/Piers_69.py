from spirit.game.card_effects.trainers import piers
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ad2c0db9-aeb3-52ba-9b9e-00e197ba14c2",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Piers.Name",
    display_name="Piers",
    searchable_by=["Piers", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="SWSH45",
    rarity=Rarities.RareUltra,
    effect=piers
)
