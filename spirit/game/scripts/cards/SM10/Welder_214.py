from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    welder,
    welder_condition,
)

card = SupporterCardDef(
    guid="fc29c62f-0299-51d5-8585-522057babbe8",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Welder.Name",
    display_name="Welder",
    searchable_by=["Welder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    condition=welder_condition,
    effect=welder
)
