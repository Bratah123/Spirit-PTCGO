from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    morty,
    morty_condition,
)

card = SupporterCardDef(
    guid="3fcfcc80-8445-5c61-9a80-8610a08e7e1f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morty.Name",
    display_name="Morty",
    searchable_by=["Morty", "Supporter"],
    subtypes=["Supporter"],
    collector_number=212,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    effect=morty,
    condition=morty_condition,
)
