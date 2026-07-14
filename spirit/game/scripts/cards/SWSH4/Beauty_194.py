from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="b2562d66-edd6-5670-8235-1451870b2d95",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Beauty.Name",
    display_name="Beauty",
    searchable_by=["Beauty", "Supporter"],
    subtypes=["Supporter"],
    collector_number=194,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    effect=draw_attack(2)
)
