"""Bebe's Search (DP2 #109)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import bebes_search, bebes_search_condition

card = SupporterCardDef(
    guid="8cd29d02-abbe-5656-87d4-2427ea69e190",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BebesSearch.Name",
    display_name="Bebe's Search",
    searchable_by=["Bebe's Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=bebes_search(),
    condition=bebes_search_condition,
)
