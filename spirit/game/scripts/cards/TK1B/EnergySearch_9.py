from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="19a85642-d843-564c-85cd-e900d350de96",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="TK1B",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1, minimum=0, reveal=True,
                           prompt="Choose a basic Energy card to put into your hand."),
)
