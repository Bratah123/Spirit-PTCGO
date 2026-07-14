from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import search_to_hand

card = SupporterCardDef(
    guid="35f9b28a-9133-5326-8256-96a1ff31a27a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lady.Name",
    display_name="Lady",
    searchable_by=["Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    effect=search_to_hand(
        is_basic_energy_card, count=4, reveal=True,
        prompt="Choose up to 4 basic Energy cards.",
    )
)
