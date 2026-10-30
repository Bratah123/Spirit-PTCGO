from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import draw_then_discard

card = SupporterCardDef(
    guid="eefe12b7-4df4-53fe-aff7-9c462b993886",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    effect=draw_then_discard(3, 1),
)
