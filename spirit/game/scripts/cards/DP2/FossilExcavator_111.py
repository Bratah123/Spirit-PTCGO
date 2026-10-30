"""Fossil Excavator (DP2 #111)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import fossil_excavator

card = SupporterCardDef(
    guid="d92deda5-9a00-588a-9e6e-0e67cc1fca1d",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavator.Name",
    display_name="Fossil Excavator",
    searchable_by=["Fossil Excavator", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=fossil_excavator(),
)
