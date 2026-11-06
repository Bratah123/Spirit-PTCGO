from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.card_effects.ecard import energy_charge_item


card = ItemCardDef(
    guid="1b0c3704-6d95-58ed-b892-a29de4a0ae54",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyCharge.Name",
    display_name="Energy Charge",
    searchable_by=["Energy Charge"],
    subtypes=[],
    collector_number=85,
    set_code="NEO1",
    rarity=Rarities.Rare,
    condition=requires_discard(is_energy_card),
    effect=energy_charge_item,
)
