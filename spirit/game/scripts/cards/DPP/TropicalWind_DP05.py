"""Tropical Wind (DPP #DP05)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import tropical_wind

card = ItemCardDef(
    guid="8fd4b34b-663b-5669-9f7a-f95f857f150f",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalWind.Name",
    display_name="Tropical Wind",
    searchable_by=["Tropical Wind", "Item"],
    subtypes=["Item"],
    collector_number=5,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    effect=tropical_wind,
)
