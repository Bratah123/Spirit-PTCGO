from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.card_effects.ex import holon_mentor, holon_mentor_condition
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="96273697-7dfc-56d8-b71f-92b917da80cb",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonMentor.Name",
    display_name="Holon Mentor",
    searchable_by=["Holon Mentor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=93,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    condition=holon_mentor_condition(),
    effect=holon_mentor()
)
