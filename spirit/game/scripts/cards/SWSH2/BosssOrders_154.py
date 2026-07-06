from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="142305e1-e17c-593d-9f1d-c69b42d9f802",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrders.Name",
    display_name="Boss's Orders",
    searchable_by=["Boss's Orders", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    effect=bosss_orders,
    condition=opponent_has_bench
)
