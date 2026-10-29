from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    sabrinas_suggestion,
)

card = SupporterCardDef(
    guid="737c6c7d-51b9-5a96-902e-21fefb7b3984",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasSuggestion.Name",
    display_name="Sabrina's Suggestion",
    searchable_by=["Sabrina's Suggestion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=65,
    set_code="HF",
    rarity=Rarities.Uncommon,
    effect=sabrinas_suggestion,
)
