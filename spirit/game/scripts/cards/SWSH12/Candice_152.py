from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import candice_predicate
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="30041b72-5bd5-5694-af91-ac5eb1e03266",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Candice.Name",
    display_name="Candice",
    searchable_by=["Candice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=152,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    effect=look_at_top(
        7, take=7, predicate=candice_predicate, rest="shuffle", minimum=0,
        prompt="Choose any number of Water Pokémon and Water Energy cards to put into your hand",
    )
)
