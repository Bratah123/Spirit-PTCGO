from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import marys_request

card = SupporterCardDef(
    guid="7aa632dd-492d-5b8d-ad8b-c79660e635cb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarysRequest.Name",
    display_name="Mary's Request",
    searchable_by=["Mary's Request", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    effect=marys_request,
)
