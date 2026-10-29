from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import (
    blaines_last_stand,
    blaines_last_stand_condition,
)

card = SupporterCardDef(
    guid="2aa98f63-7db3-5bbc-ba5c-3c8b93c9da2a",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name",
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", "Supporter"],
    subtypes=["Supporter"],
    collector_number=52,
    set_code="HF",
    rarity=Rarities.Rare,
    effect=blaines_last_stand,
    condition=blaines_last_stand_condition,
)
