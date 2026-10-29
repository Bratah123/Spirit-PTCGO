from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    sabrinas_suggestion,
)

card = SupporterCardDef(
    guid="ea70ea85-89a6-5b5b-87c8-55c229b32ed7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasSuggestion.Name",
    display_name="Sabrina's Suggestion",
    searchable_by=["Sabrina's Suggestion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=sabrinas_suggestion,
)
