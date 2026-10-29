from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    greens_exploration,
    greens_exploration_condition,
)

card = SupporterCardDef(
    guid="73897bc6-10ad-52d5-a622-e1ef9b811e14",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreensExploration.Name",
    display_name="Green's Exploration",
    searchable_by=["Green's Exploration", "Supporter"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    condition=greens_exploration_condition,
    effect=greens_exploration
)
