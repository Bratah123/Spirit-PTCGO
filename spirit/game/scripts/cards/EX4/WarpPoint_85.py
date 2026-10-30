from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import warp_point

card = ItemCardDef(
    guid="f547b3da-a516-5663-91ef-7b624b6ec279",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=warp_point,
)
