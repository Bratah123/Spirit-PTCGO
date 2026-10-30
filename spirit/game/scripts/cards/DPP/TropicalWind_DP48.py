"""Tropical Wind (DPP #DP48)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import tropical_wind

card = ItemCardDef(
    guid="6c55c12a-a9d7-5797-ac10-9cf3a99739f5",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalWind.Name",
    display_name="Tropical Wind",
    searchable_by=["Tropical Wind", "Item"],
    subtypes=["Item"],
    collector_number=48,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    effect=tropical_wind,
)
