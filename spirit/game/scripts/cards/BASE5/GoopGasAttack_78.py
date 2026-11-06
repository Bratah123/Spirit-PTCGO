from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import goop_gas_attack

card = ItemCardDef(
    guid="426a5188-2c95-5fe9-b899-3393674d10f8",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoopGasAttack.Name",
    display_name="Goop Gas Attack",
    searchable_by=["Goop Gas Attack"],
    subtypes=[],
    collector_number=78,
    set_code="BASE5",
    rarity=Rarities.Common,
    effect=goop_gas_attack,
)
