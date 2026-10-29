from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    evelyn,
    evelyn_condition,
)

card = SupporterCardDef(
    guid="2cf723f0-d7bc-5cee-81b0-216b65c1bbcd",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evelyn.Name",
    display_name="Evelyn",
    searchable_by=["Evelyn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=evelyn,
            condition=evelyn_condition,
        )
