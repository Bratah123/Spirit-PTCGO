from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect

card = ItemCardDef(
    guid="742fc928-dc88-5146-a4e9-019ea3824288",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=cure_conditions_effect("active"),
)
