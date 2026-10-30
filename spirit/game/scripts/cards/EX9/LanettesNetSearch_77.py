from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import lanettes_net_search
from spirit.game.card_effects.trainers import deck_nonempty


card = SupporterCardDef(
    guid="72952279-5dd3-51ef-b4e4-ed23fe287d86",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanettesNetSearch.Name",
    display_name="Lanette's Net Search",
    searchable_by=["Lanette's Net Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=lanettes_net_search,
    condition=deck_nonempty,
)
