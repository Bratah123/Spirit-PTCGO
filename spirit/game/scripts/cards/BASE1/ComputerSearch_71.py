from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import computer_search, computer_search_condition


card = ItemCardDef(
    guid="cbeac06c-8bf8-5c29-a596-955ff0f2445c",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search"],
    subtypes=[],
    collector_number=71,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=computer_search,
    condition=computer_search_condition,
)
