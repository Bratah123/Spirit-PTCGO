from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    giovannis_exile,
    giovannis_exile_condition,
)

card = SupporterCardDef(
    guid="2463937d-37d6-5657-aa43-c6195cfa6a5d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=giovannis_exile_condition,
    effect=giovannis_exile
)
