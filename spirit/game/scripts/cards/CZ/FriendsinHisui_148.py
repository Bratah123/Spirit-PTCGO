from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="b8aab8e6-e710-5acc-90d0-075282434464",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinHisui.Name",
    display_name="Friends in Hisui",
    searchable_by=["Friends in Hisui", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    effect=draw_attack(3)
)
