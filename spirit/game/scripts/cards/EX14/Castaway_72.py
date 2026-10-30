from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import castaway_search

card = SupporterCardDef(
    guid="e13d3738-9e26-5020-810f-a901b29d6c2b",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Castaway.Name",
    display_name="Castaway",
    searchable_by=["Castaway", "Supporter"],
    subtypes=["Supporter"],
    collector_number=72,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=castaway_search(),
)
