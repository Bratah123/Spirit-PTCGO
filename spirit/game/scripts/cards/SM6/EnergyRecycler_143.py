from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="522c6d24-1020-5d70-951e-41ae92eaf0d0",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    condition=requires_discard(is_basic_energy_card, n=5),
    effect=recover_from_discard(
        is_basic_energy_card, count=5, minimum=5, to="deck_shuffle",
        prompt="Choose 5 basic Energy to shuffle into your deck.",
    ),
)
