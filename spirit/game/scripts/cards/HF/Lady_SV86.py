from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import search_to_hand

card = SupporterCardDef(
    guid="9d694724-7791-5d1c-8ce0-343194d7b910",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lady.Name",
    display_name="Lady",
    searchable_by=["Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(
        is_basic_energy_card, count=4, reveal=True,
        prompt="Choose up to 4 basic Energy cards.",
    )
)
