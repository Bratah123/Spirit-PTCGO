from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import tropical_tidal_wave


card = ItemCardDef(
    guid="9f983769-6f1d-59d6-ac67-646e7b6337db",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalTidalWave.Name",
    display_name="Tropical Tidal Wave",
    searchable_by=["Tropical Tidal Wave", "Item"],
    subtypes=["Item"],
    collector_number=36,
    set_code="NP",
    rarity=Rarities.RarePromo,
    effect=tropical_tidal_wave,
)
