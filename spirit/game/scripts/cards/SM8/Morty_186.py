from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    morty,
    morty_condition,
)

card = SupporterCardDef(
    guid="724a30bb-19c2-58fc-8719-cb20ccaa5826",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morty.Name",
    display_name="Morty",
    searchable_by=["Morty", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=morty,
    condition=morty_condition,
)
