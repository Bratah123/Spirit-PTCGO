from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    aether_foundation_employee,
)

card = SupporterCardDef(
    guid="eed448cd-793c-57e1-9f9c-7409c6b27e7d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherFoundationEmployee.Name",
    display_name="Aether Foundation Employee",
    searchable_by=["Aether Foundation Employee", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=aether_foundation_employee
)
