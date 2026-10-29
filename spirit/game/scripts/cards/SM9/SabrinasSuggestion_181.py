from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    sabrinas_suggestion,
)

card = SupporterCardDef(
    guid="cb183046-4137-5ec9-b50a-2d557e444d09",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasSuggestion.Name",
    display_name="Sabrina's Suggestion",
    searchable_by=["Sabrina's Suggestion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=181,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=sabrinas_suggestion,
)
