from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import lass

card = ItemCardDef(
    guid="6b1a01aa-1f51-57ae-90df-798afdd9c40c",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lass.Name",
    display_name="Lass",
    searchable_by=["Lass"],
    subtypes=[],
    collector_number=104,
    set_code="BASE4",
    rarity=Rarities.Rare,
    effect=lass,
)
