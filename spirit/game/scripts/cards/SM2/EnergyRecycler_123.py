from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3ba4e70b-c3b0-5a11-99e0-f797d657a7bd",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_basic_energy_card, n=5),
    effect=recover_from_discard(
        is_basic_energy_card, count=5, minimum=5, to="deck_shuffle",
        prompt="Choose 5 basic Energy to shuffle into your deck.",
    ),
)
