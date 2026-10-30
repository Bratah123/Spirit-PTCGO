from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.card_effects.ex import holon_researcher
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="735f78ef-f7c2-523e-a612-92b4ffe40595",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonResearcher.Name",
    display_name="Holon Researcher",
    searchable_by=["Holon Researcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=holon_researcher()
)
