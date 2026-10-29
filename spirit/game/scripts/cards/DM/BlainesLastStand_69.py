from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import (
    blaines_last_stand,
    blaines_last_stand_condition,
)

card = SupporterCardDef(
    guid="361a53c3-36c7-58e9-a123-33be61c7368b",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastStand.Name",
    display_name="Blaine's Last Stand",
    searchable_by=["Blaine's Last Stand", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="DM",
    rarity=Rarities.RareUltra,
    effect=blaines_last_stand,
    condition=blaines_last_stand_condition,
)
