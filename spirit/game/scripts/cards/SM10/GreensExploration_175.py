from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    greens_exploration,
    greens_exploration_condition,
)

card = SupporterCardDef(
    guid="227a00bb-895e-553a-91d4-f11b64bfc756",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreensExploration.Name",
    display_name="Green's Exploration",
    searchable_by=["Green's Exploration", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=greens_exploration_condition,
    effect=greens_exploration
)
