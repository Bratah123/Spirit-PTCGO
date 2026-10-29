from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    hiker,
    hiker_condition,
)

card = SupporterCardDef(
    guid="5c0b86c8-f5b9-54aa-9692-2488c3ecc3c8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hiker.Name",
    display_name="Hiker",
    searchable_by=["Hiker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=hiker,
    condition=hiker_condition,
)
