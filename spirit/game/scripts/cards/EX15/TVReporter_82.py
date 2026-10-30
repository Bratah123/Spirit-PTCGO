from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import draw_then_discard

card = SupporterCardDef(
    guid="62b7467d-2557-5e13-af29-cfe72c3c0243",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=draw_then_discard(3, 1),
)
