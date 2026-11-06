from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    giovannis_last_resort,
    giovannis_last_resort_condition,
)


card = ItemCardDef(
    guid="b909f055-1be4-5d3c-9e67-d58121a16176",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisLastResort.Name",
    display_name="Giovanni's Last Resort",
    searchable_by=["Giovanni's Last Resort"],
    subtypes=[],
    collector_number=105,
    set_code="GYM2",
    rarity=Rarities.Rare,
    condition=giovannis_last_resort_condition,
    effect=giovannis_last_resort,
)
