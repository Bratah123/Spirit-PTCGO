from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (
    flip_discard_opponent_energy,
    opponent_has_energy_attached,
)


card = ItemCardDef(
    guid="3afde8ac-a739-5561-9ec9-a302835b8e78",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2", "Item"],
    subtypes=["Item"],
    collector_number=74,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    condition=opponent_has_energy_attached,
    effect=flip_discard_opponent_energy("Energy Removal 2"),
)
