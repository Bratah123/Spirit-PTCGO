"""Poké Blower + (DP7 #88)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import poke_blower_plus

card = ItemCardDef(
    guid="0c49c6ac-6d99-5347-a613-b05dc7eb95e3",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBlower.Name",
    display_name="Poké Blower +",
    searchable_by=["Poké Blower +", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=poke_blower_plus(),
)
