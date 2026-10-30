from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import lanettes_net_search
from spirit.game.card_effects.trainers import deck_nonempty


card = SupporterCardDef(
    guid="bcb48bd8-729f-576e-bd58-e1f97cb26749",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanettesNetSearch.Name",
    display_name="Lanette's Net Search",
    searchable_by=["Lanette's Net Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    effect=lanettes_net_search,
    condition=deck_nonempty,
)
