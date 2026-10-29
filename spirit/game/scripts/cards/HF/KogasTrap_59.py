from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    kogas_trap,
)

card = SupporterCardDef(
    guid="e9112bd6-8e01-5f66-b1c7-caed7b635293",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KogasTrap.Name",
    display_name="Koga's Trap",
    searchable_by=["Koga's Trap", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="HF",
    rarity=Rarities.Uncommon,
    effect=kogas_trap
)
