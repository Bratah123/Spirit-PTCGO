from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect

card = SupporterCardDef(
    guid="ce41c09a-a66c-5959-98cd-954962c857d0",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bianca.Name",
    display_name="Bianca",
    searchable_by=["Bianca", "Supporter"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="BW7",
    rarity=Rarities.RareUltra,
    effect=draw_until_effect(6)
)
