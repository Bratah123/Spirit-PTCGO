from spirit.game.card_effects.trainers import piers
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="fb9b5d7e-1924-568a-b511-a065c3305125",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Piers.Name",
    display_name="Piers",
    searchable_by=["Piers", "Supporter"],
    subtypes=["Supporter"],
    collector_number=58,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=piers
)
