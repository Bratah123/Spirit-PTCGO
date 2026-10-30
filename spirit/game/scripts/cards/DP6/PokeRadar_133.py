"""Poké Radar (DP6 #133)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import poke_radar

card = ItemCardDef(
    guid="c8e5bfee-d222-5d51-84c1-ab0b05f1a45a",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeRadar.Name",
    display_name="Poké Radar",
    searchable_by=["Poké Radar", "Item"],
    subtypes=["Item"],
    collector_number=133,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    effect=poke_radar(),
)
