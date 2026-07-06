from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import energy_recycler, has_basic_energy_in_discard

card = ItemCardDef(
    guid="3a21a8d8-905f-558f-a17e-213df3557328",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    condition=has_basic_energy_in_discard,
    effect=energy_recycler,
)
