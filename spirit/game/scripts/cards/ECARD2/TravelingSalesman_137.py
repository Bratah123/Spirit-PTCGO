from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.ecard import is_tm_or_tool


card = SupporterCardDef(
    guid="c0fe7623-f237-5205-a417-776add2aaa3b",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TravelingSalesman.Name",
    display_name="Traveling Salesman",
    searchable_by=["Traveling Salesman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_tm_or_tool, count=2, minimum=0, reveal=True,
        prompt="Choose up to 2 Technical Machine and/or Pokémon Tool cards.",
    ),
)
