from spirit.game.card_effects.trainers import piers
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b298dc96-97e3-51c7-81d0-19ab6457f4be",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Piers.Name",
    display_name="Piers",
    searchable_by=["Piers", "Supporter"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    effect=piers
)
