from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import tropical_tidal_wave


card = ItemCardDef(
    guid="27a734ae-6cc5-5c1d-8932-44b5faaf0471",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TropicalTidalWave.Name",
    display_name="Tropical Tidal Wave",
    searchable_by=["Tropical Tidal Wave", "Item"],
    subtypes=["Item"],
    collector_number=27,
    set_code="NP",
    rarity=Rarities.RarePromo,
    effect=tropical_tidal_wave,
)
