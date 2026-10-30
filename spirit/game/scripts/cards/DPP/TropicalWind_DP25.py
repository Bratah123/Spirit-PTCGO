"""Tropical Wind (DPP #DP25)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import tropical_wind

card = ItemCardDef(
    guid="8420000c-d47f-5caf-a3f1-73fd7547a6c9",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalWind.Name",
    display_name="Tropical Wind",
    searchable_by=["Tropical Wind", "Item"],
    subtypes=["Item"],
    collector_number=25,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    effect=tropical_wind,
)
