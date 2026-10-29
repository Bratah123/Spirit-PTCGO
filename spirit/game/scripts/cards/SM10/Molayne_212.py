from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    molayne,
    molayne_condition,
)

card = SupporterCardDef(
    guid="4db8befe-b191-5726-a9b3-46d9ff359f7a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Molayne.Name",
    display_name="Molayne",
    searchable_by=["Molayne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=212,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    condition=molayne_condition,
    effect=molayne
)
