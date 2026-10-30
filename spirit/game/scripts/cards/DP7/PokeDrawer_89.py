"""Poké Drawer + (DP7 #89)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import poke_drawer_plus

card = ItemCardDef(
    guid="f1a46bc0-2d62-57ca-9d89-3dfde732b8d0",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeDrawer.Name",
    display_name="Poké Drawer +",
    searchable_by=["Poké Drawer +", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=poke_drawer_plus(),
)
