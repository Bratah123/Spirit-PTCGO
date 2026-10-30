from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (
    flip_discard_opponent_energy,
    opponent_has_energy_attached,
)


card = ItemCardDef(
    guid="e7b03854-ca7c-585a-b33b-78e45995c8b2",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    condition=opponent_has_energy_attached,
    effect=flip_discard_opponent_energy("Energy Removal 2"),
)
