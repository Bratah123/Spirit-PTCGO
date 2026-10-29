from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    welder,
    welder_condition,
)

card = SupporterCardDef(
    guid="94ab2c0e-e254-5d26-90ae-ad25737d73bd",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Welder.Name",
    display_name="Welder",
    searchable_by=["Welder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=welder_condition,
    effect=welder
)
