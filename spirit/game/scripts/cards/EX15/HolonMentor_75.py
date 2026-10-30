from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.card_effects.ex import holon_mentor, holon_mentor_condition
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="56487d85-6838-5dbc-950b-643b06ce73c8",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonMentor.Name",
    display_name="Holon Mentor",
    searchable_by=["Holon Mentor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    condition=holon_mentor_condition(),
    effect=holon_mentor()
)
