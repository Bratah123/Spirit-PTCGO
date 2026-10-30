"""Poké Healer + (DP7 #90)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import poke_healer_plus

card = ItemCardDef(
    guid="8b781dff-5511-5088-8e93-eee4ccf49dd5",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeHealer.Name",
    display_name="Poké Healer +",
    searchable_by=["Poké Healer +", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=poke_healer_plus(),
)
