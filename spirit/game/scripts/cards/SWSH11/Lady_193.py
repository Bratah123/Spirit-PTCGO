from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import search_to_hand

card = SupporterCardDef(
    guid="f9a504c9-030d-5c62-ad05-1a6e1f3a6052",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lady.Name",
    display_name="Lady",
    searchable_by=["Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=193,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(
        is_basic_energy_card, count=4, reveal=True,
        prompt="Choose up to 4 basic Energy cards.",
    )
)
