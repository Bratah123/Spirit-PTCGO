from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import warp_point

card = ItemCardDef(
    guid="db3b7b0e-8837-53a7-b762-aea55f1f4720",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=warp_point,
)
