from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    electropower,
)

card = ItemCardDef(
    guid="5ac0501b-4682-5255-b24f-744b6dcddaa2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electropower.Name",
    display_name="Electropower",
    searchable_by=["Electropower", "Item"],
    subtypes=["Item"],
    collector_number=237,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=electropower
)
