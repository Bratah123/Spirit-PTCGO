from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import energy_charge

card = ItemCardDef(
    guid="f19d4531-d8d0-579d-a216-292a4d5510a9",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyCharge.Name",
    display_name="Energy Charge",
    searchable_by=["Energy Charge", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    effect=energy_charge,
)
