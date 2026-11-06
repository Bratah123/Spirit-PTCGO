from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import computer_search, computer_search_condition


card = ItemCardDef(
    guid="7c865218-6d19-5016-b199-e353d3542aff",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search"],
    subtypes=[],
    collector_number=101,
    set_code="BASE4",
    rarity=Rarities.Rare,
    effect=computer_search,
    condition=computer_search_condition,
)
