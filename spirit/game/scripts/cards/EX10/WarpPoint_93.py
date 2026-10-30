from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import warp_point

card = ItemCardDef(
    guid="8fd3b23a-a76e-53b6-b28a-de2314b6bd33",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    effect=warp_point,
)
