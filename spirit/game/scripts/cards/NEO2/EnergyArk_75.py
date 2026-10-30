from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import energy_ark


card = ItemCardDef(
    guid="67633335-3ee9-55b9-a277-d19f7bee9c65",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyArk.Name",
    display_name="Energy Ark",
    searchable_by=["Energy Ark"],
    subtypes=[],
    collector_number=75,
    set_code="NEO2",
    rarity=Rarities.Common,
    effect=energy_ark,
)
