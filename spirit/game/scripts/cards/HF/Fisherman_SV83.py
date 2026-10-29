from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    fisherman,
    fisherman_condition,
)

card = SupporterCardDef(
    guid="1ed0d286-2d5e-55d5-a48d-3a5dab10626e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=152,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=fisherman,
    condition=fisherman_condition,
)
