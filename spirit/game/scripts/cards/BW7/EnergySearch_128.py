from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d748ddc7-09cf-5475-8f8a-d60b037049c7",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="BW7",
    rarity=Rarities.Common,
    effect=search_to_hand(
        is_basic_energy_card, count=1, minimum=0, reveal=True,
        prompt="Choose a basic Energy card to put into your hand.",
    ),
)
