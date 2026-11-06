from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import escape_rope


card = ItemCardDef(
    guid="ef7ff778-e9c7-5a1c-bc15-f4dae5db4b02",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point"],
    subtypes=[],
    collector_number=152,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=escape_rope,
)
