from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    energy_spinner,
)

card = ItemCardDef(
    guid="db1ba32a-1034-5a63-b73d-1597c45a988e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySpinner.Name",
    display_name="Energy Spinner",
    searchable_by=["Energy Spinner", "Item"],
    subtypes=["Item"],
    collector_number=170,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=energy_spinner
)
