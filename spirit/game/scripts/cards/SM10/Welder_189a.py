from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    welder,
    welder_condition,
)

card = SupporterCardDef(
    guid="11313ba3-eb2d-50d4-ae61-7eb950f59c85",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Welder.Name",
    display_name="Welder",
    searchable_by=["Welder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=237,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=welder_condition,
    effect=welder
)
