from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.card_effects.ex import holon_scientist
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="195a4523-8cb3-5d4f-94fa-3f77d04ac369",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonScientist.Name",
    display_name="Holon Scientist",
    searchable_by=["Holon Scientist", "Supporter"],
    subtypes=["Supporter"],
    collector_number=97,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=holon_scientist()
)
