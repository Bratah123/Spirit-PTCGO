from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import giovanni, giovanni_condition


card = ItemCardDef(
    guid="43919234-6fbb-5ffa-b663-001b09ab8cd4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giovanni.Name",
    display_name="Giovanni",
    searchable_by=["Giovanni"],
    subtypes=[],
    collector_number=18,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    condition=giovanni_condition,
    effect=giovanni,
)
