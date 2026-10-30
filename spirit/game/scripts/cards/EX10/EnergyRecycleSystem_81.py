from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import energy_recycle_system

card = ItemCardDef(
    guid="63125fd1-a742-5c7b-b5a1-8b78cec0206d",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name",
    display_name="Energy Recycle System",
    searchable_by=["Energy Recycle System", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    effect=energy_recycle_system(),
)
