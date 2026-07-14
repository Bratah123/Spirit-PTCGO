from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="89e8f9b7-0e7d-5063-8e1c-29472836845a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cook.Name",
    display_name="Cook",
    searchable_by=["Cook", "Supporter"],
    subtypes=["Supporter"],
    collector_number=228,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=heal_item(70, scope="active"),
)
