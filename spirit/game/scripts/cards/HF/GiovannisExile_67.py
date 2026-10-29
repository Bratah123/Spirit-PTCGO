from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    giovannis_exile,
    giovannis_exile_condition,
)

card = SupporterCardDef(
    guid="de71ea3b-caf7-5879-adba-979ca5582ede",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisExile.Name",
    display_name="Giovanni's Exile",
    searchable_by=["Giovanni's Exile", "Supporter"],
    subtypes=["Supporter"],
    collector_number=67,
    set_code="HF",
    rarity=Rarities.RareUltra,
    condition=giovannis_exile_condition,
    effect=giovannis_exile
)
