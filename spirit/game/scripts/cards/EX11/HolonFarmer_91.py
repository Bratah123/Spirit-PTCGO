from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.card_effects.ex import holon_farmer
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="38f2715f-12ae-5e96-9eb4-6ec4a2aa8e65",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonFarmer.Name",
    display_name="Holon Farmer",
    searchable_by=["Holon Farmer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=91,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=holon_farmer()
)
