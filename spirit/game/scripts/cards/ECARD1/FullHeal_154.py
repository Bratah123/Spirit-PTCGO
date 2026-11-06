from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect

card = ItemCardDef(
    guid="e150f477-7bda-5a72-9e4a-0907f01e7e9c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal"],
    subtypes=[],
    collector_number=154,
    set_code="ECARD1",
    rarity=Rarities.Common,
    effect=cure_conditions_effect("active")
)
