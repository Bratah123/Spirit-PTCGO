from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

card = SupporterCardDef(
    guid="a5fe7301-9ce8-5306-9878-561618f00324",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cilan.Name",
    display_name="Cilan",
    searchable_by=["Cilan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_basic_energy_card, count=3, reveal=True,
        prompt="Choose up to 3 basic Energy cards to put into your hand.",
    )
)
