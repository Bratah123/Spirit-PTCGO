from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect

card = ItemCardDef(
    guid="b74e0d98-d02b-5b18-8527-d8afd24ebf08",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=51,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=cure_conditions_effect("active")
)
