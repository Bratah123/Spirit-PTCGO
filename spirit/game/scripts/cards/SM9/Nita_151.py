from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    nita,
    nita_condition,
)

card = SupporterCardDef(
    guid="03b884f8-71a8-568c-af53-370d48ae2ebb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nita.Name",
    display_name="Nita",
    searchable_by=["Nita", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=nita,
            condition=nita_condition,
        )
