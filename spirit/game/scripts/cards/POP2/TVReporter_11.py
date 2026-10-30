from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import draw_then_discard

card = SupporterCardDef(
    guid="89ef67e0-8fe8-5107-a6ce-3cbd3ea62bd9",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=11,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    effect=draw_then_discard(3, 1),
)
