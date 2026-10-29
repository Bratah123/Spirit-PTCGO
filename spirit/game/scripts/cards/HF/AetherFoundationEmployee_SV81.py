from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    aether_foundation_employee,
)

card = SupporterCardDef(
    guid="e0372110-c3c6-5305-a6ca-fdfeeee25b82",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherFoundationEmployee.Name",
    display_name="Aether Foundation Employee",
    searchable_by=["Aether Foundation Employee", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=aether_foundation_employee
)
