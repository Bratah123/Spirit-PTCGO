from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect

card = ItemCardDef(
    guid="ae12c97a-134a-5df1-8b38-bb69fec3580a",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal"],
    subtypes=[],
    collector_number=111,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=cure_conditions_effect("active")
)
