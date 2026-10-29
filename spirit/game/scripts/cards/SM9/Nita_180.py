from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    nita,
    nita_condition,
)

card = SupporterCardDef(
    guid="57d76f7d-3945-5fa2-9f05-70c2b717c650",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nita.Name",
    display_name="Nita",
    searchable_by=["Nita", "Supporter"],
    subtypes=["Supporter"],
    collector_number=180,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=nita,
            condition=nita_condition,
        )
