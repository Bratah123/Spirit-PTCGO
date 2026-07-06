from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5732ed77-79d4-543f-bafd-a4780a58e38d",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrders.Name",
    display_name="Boss's Orders",
    searchable_by=["Boss's Orders", "Supporter"],
    subtypes=["Supporter"],
    collector_number=58,
    set_code="SWSH45",
    rarity=Rarities.Rare,
    effect=bosss_orders,
    condition=opponent_has_bench
)
