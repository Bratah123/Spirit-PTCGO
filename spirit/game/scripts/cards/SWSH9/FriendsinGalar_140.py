from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="a2b35997-7503-5e2b-848d-b967d745fec4",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinGalar.Name",
    display_name="Friends in Galar",
    searchable_by=["Friends in Galar", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3)
)
