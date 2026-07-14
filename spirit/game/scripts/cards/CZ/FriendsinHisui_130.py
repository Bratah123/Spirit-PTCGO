from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="d48141ff-3e7c-5905-8dc4-7bee4e9abd02",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinHisui.Name",
    display_name="Friends in Hisui",
    searchable_by=["Friends in Hisui", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3)
)
