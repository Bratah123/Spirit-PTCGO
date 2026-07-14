from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import candice_predicate
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="74305ab7-fb5a-5d9e-9b70-18a1ca26ab66",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Candice.Name",
    display_name="Candice",
    searchable_by=["Candice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    effect=look_at_top(
        7, take=7, predicate=candice_predicate, rest="shuffle", minimum=0,
        prompt="Choose any number of Water Pokémon and Water Energy cards to put into your hand",
    )
)
