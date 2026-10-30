from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect

card = ItemCardDef(
    guid="8990de97-d63d-58f7-9c11-5d3b4cd030fd",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal"],
    subtypes=[],
    collector_number=82,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=cure_conditions_effect("active")
)
