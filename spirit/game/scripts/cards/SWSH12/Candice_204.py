from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import candice_predicate
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2755e261-9666-5b49-8870-adfb1c152516",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Candice.Name",
    display_name="Candice",
    searchable_by=["Candice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SWSH12",
    rarity=Rarities.RareRainbow,
    effect=look_at_top(
        7, take=7, predicate=candice_predicate, rest="shuffle", minimum=0,
        prompt="Choose any number of Water Pokémon and Water Energy cards to put into your hand",
    )
)
