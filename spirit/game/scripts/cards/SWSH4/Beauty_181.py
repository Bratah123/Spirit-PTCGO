from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="6184b061-8f6c-54a8-a9ec-887513082f34",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Beauty.Name",
    display_name="Beauty",
    searchable_by=["Beauty", "Supporter"],
    subtypes=["Supporter"],
    collector_number=181,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    effect=draw_attack(2)
)
