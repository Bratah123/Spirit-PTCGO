from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6935a07e-2951-596b-a9e6-c5735c2a3f7d",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrders.Name",
    display_name="Boss's Orders",
    searchable_by=["Boss's Orders", "Supporter"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    effect=bosss_orders,
    condition=opponent_has_bench
)
