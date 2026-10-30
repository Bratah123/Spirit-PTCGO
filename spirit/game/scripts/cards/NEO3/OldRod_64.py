from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import old_rod, old_rod_condition


card = ItemCardDef(
    guid="1d88c3b4-8160-5e7b-9a57-21c661c71984",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldRod.Name",
    display_name="Old Rod",
    searchable_by=["Old Rod"],
    subtypes=[],
    collector_number=64,
    set_code="NEO3",
    rarity=Rarities.Common,
    condition=old_rod_condition,
    effect=old_rod,
)
