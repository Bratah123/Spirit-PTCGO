from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="f67747e6-7f5b-505e-b431-ab13598e8f9e",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Beauty.Name",
    display_name="Beauty",
    searchable_by=["Beauty", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    effect=draw_attack(2)
)
