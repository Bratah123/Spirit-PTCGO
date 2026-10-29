from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import (
    blaines_last_stand,
    blaines_last_stand_condition,
)

card = SupporterCardDef(
    guid="87ce236a-7ef6-5bef-b96f-309a975d7373",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name",
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", "Supporter"],
    subtypes=["Supporter"],
    collector_number=58,
    set_code="DM",
    rarity=Rarities.RareHolo,
    effect=blaines_last_stand,
    condition=blaines_last_stand_condition,
)
