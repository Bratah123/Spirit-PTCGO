from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2931b336-c870-5403-b178-933d0e7905d4",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search"],
    subtypes=[],
    collector_number=59,
    set_code="BASE3",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1, minimum=0, reveal=True,
                           prompt="Choose a basic Energy card to put into your hand."),
)
