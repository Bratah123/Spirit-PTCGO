from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect

card = SupporterCardDef(
    guid="b1d69e59-cd80-5f05-8cf2-8fdaff6ae704",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bianca.Name",
    display_name="Bianca",
    searchable_by=["Bianca", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    effect=draw_until_effect(6)
)
