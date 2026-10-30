from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import escape_rope, someone_has_bench


card = ItemCardDef(
    guid="7a2778a7-31ec-5e8c-b37b-418e1b4e2274",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point"],
    subtypes=[],
    collector_number=126,
    set_code="GYM2",
    rarity=Rarities.Common,
    condition=someone_has_bench,
    effect=escape_rope,
)
