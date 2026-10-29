from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    samson_oak,
)

card = SupporterCardDef(
    guid="23e345e9-9e38-5bdd-8e07-46ddf59d6d1e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SamsonOak.Name",
    display_name="Samson Oak",
    searchable_by=["Samson Oak", "Supporter"],
    subtypes=["Supporter"],
    collector_number=185,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=samson_oak
)
