from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect

card = SupporterCardDef(
    guid="179fe31d-049f-5e10-8427-fad96e34a623",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bianca.Name",
    display_name="Bianca",
    searchable_by=["Bianca", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=draw_until_effect(6)
)
