from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import tropical_wind


card = ItemCardDef(
    guid="c180d9b7-1b4f-5be6-8e9a-6725df06f31e",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalWind.Name",
    display_name="Tropical Wind",
    searchable_by=["Tropical Wind", "Item"],
    subtypes=["Item"],
    collector_number=26,
    set_code="NP",
    rarity=Rarities.RarePromo,
    effect=tropical_wind,
)
