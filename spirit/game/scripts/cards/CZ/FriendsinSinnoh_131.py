from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="f869e481-4a46-5266-901b-900e2022f3ab",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinSinnoh.Name",
    display_name="Friends in Sinnoh",
    searchable_by=["Friends in Sinnoh", "Supporter"],
    subtypes=["Supporter"],
    collector_number=131,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3)
)
