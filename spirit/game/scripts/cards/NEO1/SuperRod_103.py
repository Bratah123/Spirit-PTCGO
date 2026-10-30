from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import super_rod, super_rod_condition


card = ItemCardDef(
    guid="5c8e39bb-40ac-5a2b-8dc4-8a6e77911cfd",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod"],
    subtypes=[],
    collector_number=103,
    set_code="NEO1",
    rarity=Rarities.Common,
    condition=super_rod_condition,
    effect=super_rod,
)
