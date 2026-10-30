"""Bebe's Search (DP2 #109)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import bebes_search, bebes_search_condition

card = SupporterCardDef(
    guid="PLACEHOLDER",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BebesSearch.Name",
    display_name="Bebe's Search",
    searchable_by=["Bebe's Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=bebes_search(),
    condition=bebes_search_condition,
)
