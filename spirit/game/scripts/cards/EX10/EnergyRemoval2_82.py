from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (
    flip_discard_opponent_energy,
    opponent_has_energy_attached,
)


card = ItemCardDef(
    guid="4cbfcff4-9545-574a-838a-42abcaae05dd",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    condition=opponent_has_energy_attached,
    effect=flip_discard_opponent_energy("Energy Removal 2"),
)
