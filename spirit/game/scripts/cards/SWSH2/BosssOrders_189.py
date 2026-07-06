from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6bf73995-dba1-5433-bc30-fbbd15d6d282",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrders.Name",
    display_name="Boss's Orders",
    searchable_by=["Boss's Orders", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    effect=bosss_orders,
    condition=opponent_has_bench
)
