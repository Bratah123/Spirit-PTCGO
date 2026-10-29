from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    giovannis_exile,
    giovannis_exile_condition,
)

card = SupporterCardDef(
    guid="b81603de-d01a-550f-b459-e432994f862a",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=57,
    set_code="HF",
    rarity=Rarities.Uncommon,
    condition=giovannis_exile_condition,
    effect=giovannis_exile
)
