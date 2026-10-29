from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    kogas_trap,
)

card = SupporterCardDef(
    guid="fe0d8b54-8354-5e00-b2bc-14ee250a1450",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KogasTrap.Name",
    display_name="Koga's Trap",
    searchable_by=["Koga's Trap", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=kogas_trap
)
