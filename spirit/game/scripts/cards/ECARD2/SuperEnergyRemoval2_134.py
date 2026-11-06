from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import super_energy_removal_2


card = ItemCardDef(
    guid="50ff5f7d-665a-5af0-b15e-5321358a14f4",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRemoval2.Name",
    display_name="Super Energy Removal 2",
    searchable_by=["Super Energy Removal 2"],
    subtypes=[],
    collector_number=134,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=super_energy_removal_2,
)
