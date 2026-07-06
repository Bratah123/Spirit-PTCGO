from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="06f16ae2-2712-59dc-89e4-75b957feb084",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrders.Name",
    display_name="Boss's Orders",
    searchable_by=["Boss's Orders", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="SWSH2",
    rarity=Rarities.RareRainbow,
    effect=bosss_orders,
    condition=opponent_has_bench
)
